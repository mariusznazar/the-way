"""Which script a method's command runs, where its program is a Python interpreter (WAY-105).

The gate, when it runs an invariant's method whose program is a Python interpreter, reports the
entry `unchecked` for want of a declared or produced command where the script the command runs
does not exist on the commit being checked, or `error` where that script exists on the commit the
branch left the main branch from; no format guard judges whether a command's script exists
(WAY-63, WAY-105). This module reads the script such a command runs; running the method, looking
for the script and reporting the result are the gate's, which does not exist yet.

A command is read as a POSIX shell splits it into words, quotes, backslashes and operators
included: `;`, `|`, `&` or a newline end the command, written with spaces or without, so `&>` is
`&` followed by `>`; a redirection (`>`, `>>`, `<`, `>&` and the rest) takes the word after it, and
a number written against it, as in `2>err.txt`, names a file descriptor; `#` begins a comment only
at the start of a word. A command that substitutes a command (`$(`, a backtick), quotes with `$'`
or holds `<<<` is one the reader cannot read as the shell would, and raises ValueError. Where the
first word names a Python interpreter — `python`, `python3`, `python3.<minor>` or `py`, with or
without `.exe` — the script is the first word after the interpreter's own options and the values
they take: `-W` and `-X` take one, attached or as the next word, and so does
`--check-hash-based-pycs`; `--` ends the options; `py` takes a version first, as `-3`, `-3.14`,
`-3.14-64` or `-V:<tag>`. A command that runs code given in it (`-c`), a module (`-m`) or standard
input (`-`, or no word at all) runs no script, nor does a command whose program is no Python
interpreter, or whose script word is a value the gate fills in, such as `{fork-point}`.
"""

import re

INTERPRETER = re.compile(r"python(?:\d+(?:\.\d+)?)?|py")
EXE = ".exe"
# The launcher's choice of a version, which `py` takes before the interpreter's options.
LAUNCHER_VERSION = re.compile(r"-(?:\d+(?:\.\d+)?(?:-(?:32|64|arm64))?|V:\S+)")
# Short options of the interpreter that take a value, and those that end its options with no script.
TAKES_VALUE = "WX"
NO_SCRIPT = "cm"
LONG_TAKES_VALUE = ("--check-hash-based-pycs",)
GATE_VALUE = re.compile(r"\{[a-z-]+\}")
# The operators of a POSIX shell, longest first. A redirection takes the word after it, and a
# number written against it names a file descriptor; any other operator ends the command.
OPERATORS = (">>", "<<", ">&", "<&", "<>", ">|", "&&", "||", ";;", ";", "&", "|", "(", ")",
             "<", ">")
REDIRECTIONS = (">>", "<<", ">&", "<&", "<>", ">|", "<", ">")
OPERATOR_START = ";&|()<>"
BLANKS = " \t"
NEWLINE = "\n"
BACKSLASH = "\\"
# What a backslash escapes inside double quotes; before any other character it stays.
ESCAPED_IN_DOUBLE = "$`\"\\\n"


def program_of(word):
    """The name of the program a word names, without a `.exe` suffix in any case."""
    return word[:-len(EXE)] if word.lower().endswith(EXE) else word


def tokens_of(command):
    """The tokens a POSIX shell reads in `command`, as (is it an operator, text): words with their
    quotes and backslashes removed, and operators, a newline read as `;`. A `#` at the start of a
    word begins a comment, which runs to the end of the line. A command with an unclosed quote, or
    ending in a backslash, or one that substitutes a command (`$(`, a backtick) or quotes with `$'`
    or `<<<`, which the reader cannot read as the shell would, raises ValueError."""
    tokens = []
    word, started, quoted = [], False, False
    index, length = 0, len(command)

    def end_word():
        nonlocal word, started, quoted
        if started:
            tokens.append((False, "".join(word)))
        word, started, quoted = [], False, False

    while index < length:
        char = command[index]
        if char in BLANKS:
            end_word()
            index += 1
        elif char == NEWLINE:
            end_word()
            tokens.append((True, ";"))
            index += 1
        elif char == "`" or command.startswith(("$(", "$'"), index):
            raise ValueError("the command substitutes or quotes with %s, which the reader does not "
                             "expand" % command[index:index + 2].rstrip())
        elif char == "#" and not started:
            end = command.find(NEWLINE, index)
            index = length if end < 0 else end
        elif char == BACKSLASH:
            if index + 1 >= length:
                raise ValueError("the command ends in a backslash")
            if command[index + 1] != NEWLINE:      # a backslash before a newline joins the lines
                word.append(command[index + 1])
                started = quoted = True
            index += 2
        elif char == "'":
            end = command.find("'", index + 1)
            if end < 0:
                raise ValueError("no closing quotation")
            word.append(command[index + 1:end])
            started = quoted = True
            index = end + 1
        elif char == '"':
            index += 1
            while True:
                if index >= length:
                    raise ValueError("no closing quotation")
                char = command[index]
                if char == '"':
                    break
                if char == "`" or command.startswith("$(", index):
                    raise ValueError("the command substitutes inside double quotes, which the "
                                     "reader does not expand")
                after = command[index + 1:index + 2]
                if char == BACKSLASH and after and after in ESCAPED_IN_DOUBLE:
                    if after != NEWLINE:
                        word.append(command[index + 1])
                    index += 2
                else:
                    word.append(char)
                    index += 1
            started = quoted = True
            index += 1
        elif command.startswith("<<<", index):
            raise ValueError("the command holds `<<<`, which no POSIX shell reads")
        elif char in OPERATOR_START:
            operator = next(each for each in OPERATORS if command.startswith(each, index))
            if (operator in REDIRECTIONS and started and not quoted
                    and "".join(word).isdigit()):
                word, started = [], False       # a file descriptor, not a word
            end_word()
            tokens.append((True, operator))
            index += len(operator)
        else:
            word.append(char)
            started = True
            index += 1
    end_word()
    return tokens


def words_of(command):
    """The words of the first command a POSIX shell reads in `command`, its redirections left out.
    A command a shell cannot split, as one with an unclosed quote, raises ValueError."""
    words, skip = [], False
    for operator, text in tokens_of(command):
        if skip:
            skip = False
        elif operator and text in REDIRECTIONS:
            skip = True
        elif operator:
            break
        else:
            words.append(text)
    return words


def script_of(command):
    """The path of the script `command` runs, as written, or None where its program is no Python
    interpreter or it runs no script. A command a shell cannot split raises ValueError."""
    words = words_of(command)
    if not words or not INTERPRETER.fullmatch(program_of(words[0])):
        return None
    index = 1
    if program_of(words[0]) == "py" and index < len(words) and LAUNCHER_VERSION.fullmatch(words[1]):
        index += 1
    while index < len(words):
        word = words[index]
        if word == "--":
            index += 1
            break
        if word == "-" or not word.startswith("-"):
            break
        if word.startswith("--"):
            index += 2 if word in LONG_TAKES_VALUE else 1
            continue
        flags = word[1:]
        for position, flag in enumerate(flags):
            if flag in NO_SCRIPT:
                return None
            if flag in TAKES_VALUE:
                if position == len(flags) - 1:
                    index += 1      # the value is the next word
                break
        index += 1
    if index >= len(words) or words[index] == "-" or GATE_VALUE.fullmatch(words[index]):
        return None
    return words[index]
