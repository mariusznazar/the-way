# Environment facts

What the-way takes as true about the world outside it, each with its method of checking. The rules
of an entry stand in `elements/environment-facts/template.md`.

## git-path-patterns/1

Git matches a path pattern of an attributes file by the rules of `.gitignore` patterns, except that a negative pattern is forbidden and a pattern that matches a directory does not match the paths inside it.

- **Holds for:** git 2.55.0
- **Source:** https://git-scm.com/docs/gitattributes/2.55.0 § DESCRIPTION — "The rules by which the pattern matches paths are the same as in .gitignore files (see gitignore[5]), with a few exceptions:" · § DESCRIPTION — "negative patterns are forbidden" · § DESCRIPTION — "patterns that match a directory do not recursively match paths inside that directory (so using the trailing-slash path/ syntax is pointless in an attributes file; use path/** instead)"; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py elements/environment-facts/probes/git-path-patterns --record .runs/fact-git-path-patterns.jsonl`
- **Correction:** none

## gitignore-paths/1

Within one level of precedence of its gitignore sources, the last pattern that matches a path decides whether git ignores it, and a file whose parent directory is excluded cannot be re-included.

- **Holds for:** git 2.55.0
- **Source:** https://git-scm.com/docs/gitignore/2.55.0 § DESCRIPTION — "within one level of precedence, the last matching pattern decides the outcome" · § PATTERN FORMAT — "It is not possible to re-include a file if a parent directory of that file is excluded."; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py elements/environment-facts/probes/gitignore-paths --record .runs/fact-gitignore-paths.jsonl`
- **Correction:** none

## sha-256/1

The Secure Hash Standard specifies SHA-256, whose final result is a 256-bit message digest, in its section 6.2.

- **Holds for:** FIPS 180-4 (August 2015)
- **Source:** https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf § 6.2 — "The final result of SHA-256 is a 256-bit message digest."; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py elements/environment-facts/probes/sha-256 --record .runs/fact-sha-256.jsonl`
- **Correction:** none

## utf-8/1

UTF-8 encodes every character of the range U+0000..U+10FFFF in a sequence of one to four octets.

- **Holds for:** RFC 3629 (November 2003)
- **Source:** https://www.rfc-editor.org/rfc/rfc3629.html § 3 — "In UTF-8, characters from the U+0000..U+10FFFF range (the UTF-16 accessible range) are encoded using sequences of 1 to 4 octets."; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py elements/environment-facts/probes/utf-8 --record .runs/fact-utf-8.jsonl`
- **Correction:** none

## json-text/1

A JSON text is a serialized value, in which numeric values that the grammar cannot represent, such as Infinity and NaN, are not permitted and the names within an object should be unique.

- **Holds for:** RFC 8259 (December 2017)
- **Source:** https://www.rfc-editor.org/rfc/rfc8259.html § 2 — "A JSON text is a serialized value." · § 6 — "Numeric values that cannot be represented in the grammar below (such as Infinity and NaN) are not permitted." · § 4 — "The names within an object SHOULD be unique."; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py elements/environment-facts/probes/json-text --record .runs/fact-json-text.jsonl`
- **Correction:** none

## json-lines/1

A JSON Lines file holds one valid JSON value on each line, ends each line with '\n', which admits '\r\n', and may omit the terminator after the last value.

- **Holds for:** JSON Lines, which jsonlines.org publishes without versions
- **Source:** https://jsonlines.org/ (archived: http://web.archive.org/web/20260918132122/https://jsonlines.org/, 2026-09-18) § 2 — "Each Line is a Valid JSON Value" · § 3 — "Line Terminator is '\n'" · § 3 — "This means '\r\n' is also supported because surrounding white space is implicitly ignored when parsing JSON values. Including a line terminator after the last JSON value in a file is strongly recommended but not required."; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py elements/environment-facts/probes/json-lines --record .runs/fact-json-lines.jsonl`
- **Correction:** none

## python-stdlib-modules/1

The standard library of Python 3.14 holds the modules that `sys.stdlib_module_names` names in a Python 3.14 interpreter, which lists them the same on all platforms, names only the main package of each package, and excludes test modules.

- **Holds for:** CPython 3.14, whose documentation docs.python.org publishes for the 3.14 series with no page for each bugfix release
- **Source:** https://docs.python.org/3.14/library/sys.html (archived: http://web.archive.org/web/20260907072947/https://docs.python.org/3.14/library/sys.html, 2026-09-07) § sys.stdlib_module_names — "A frozenset of strings containing the names of standard library modules." · § sys.stdlib_module_names — "It is the same on all platforms. Modules which are not available on some platforms and modules disabled at Python build are also listed. All module kinds are listed: pure Python, built-in, frozen and extension modules. Test modules are excluded." · § sys.stdlib_module_names — "For packages, only the main package is listed: sub-packages and sub-modules are not listed."; read 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py elements/environment-facts/probes/python-stdlib-modules --record .runs/fact-python-stdlib-modules.jsonl`
- **Correction:** none

## dequelabs-axe-core-visibility/1

The repository dequelabs/axe-core on github.com is public.

- **Holds for:** the repository dequelabs/axe-core on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/dequelabs/axe-core` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py elements/environment-facts/probes/dequelabs-axe-core-visibility --record .runs/fact-dequelabs-axe-core-visibility.jsonl`
- **Correction:** none

## github-spec-kit-visibility/1

The repository github/spec-kit on github.com is public.

- **Holds for:** the repository github/spec-kit on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/github/spec-kit` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py elements/environment-facts/probes/github-spec-kit-visibility --record .runs/fact-github-spec-kit-visibility.jsonl`
- **Correction:** none

## doorstop-dev-doorstop-visibility/1

The repository doorstop-dev/doorstop on github.com is public.

- **Holds for:** the repository doorstop-dev/doorstop on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/doorstop-dev/doorstop` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py elements/environment-facts/probes/doorstop-dev-doorstop-visibility --record .runs/fact-doorstop-dev-doorstop-visibility.jsonl`
- **Correction:** none

## obi1kenobi-cargo-semver-checks-visibility/1

The repository obi1kenobi/cargo-semver-checks on github.com is public.

- **Holds for:** the repository obi1kenobi/cargo-semver-checks on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/obi1kenobi/cargo-semver-checks` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py elements/environment-facts/probes/obi1kenobi-cargo-semver-checks-visibility --record .runs/fact-obi1kenobi-cargo-semver-checks-visibility.jsonl`
- **Correction:** none

## shopify-packwerk-visibility/1

The repository Shopify/packwerk on github.com is public.

- **Holds for:** the repository Shopify/packwerk on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/Shopify/packwerk` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py elements/environment-facts/probes/shopify-packwerk-visibility --record .runs/fact-shopify-packwerk-visibility.jsonl`
- **Correction:** none

## backstage-backstage-visibility/1

The repository backstage/backstage on github.com is public.

- **Holds for:** the repository backstage/backstage on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/backstage/backstage` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py elements/environment-facts/probes/backstage-backstage-visibility --record .runs/fact-backstage-backstage-visibility.jsonl`
- **Correction:** none

## kubernetes-enhancements-visibility/1

The repository kubernetes/enhancements on github.com is public.

- **Holds for:** the repository kubernetes/enhancements on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/kubernetes/enhancements` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py elements/environment-facts/probes/kubernetes-enhancements-visibility --record .runs/fact-kubernetes-enhancements-visibility.jsonl`
- **Correction:** none

## owasp-pytm-visibility/1

The repository OWASP/pytm on github.com is public.

- **Holds for:** the repository OWASP/pytm on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/OWASP/pytm` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py elements/environment-facts/probes/owasp-pytm-visibility --record .runs/fact-owasp-pytm-visibility.jsonl`
- **Correction:** none

## oasdiff-oasdiff-visibility/1

The repository oasdiff/oasdiff on github.com is public.

- **Holds for:** the repository oasdiff/oasdiff on github.com, for which github.com gives no version
- **Source:** observed: `curl https://api.github.com/repos/oasdiff/oasdiff` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py elements/environment-facts/probes/oasdiff-oasdiff-visibility --record .runs/fact-oasdiff-oasdiff-visibility.jsonl`
- **Correction:** none

## chromium-src-visibility/1

The repository chromium/src on chromium.googlesource.com opens to a reader who is not signed in.

- **Holds for:** the repository chromium/src on chromium.googlesource.com, for which the host gives no version
- **Source:** observed: `curl https://chromium.googlesource.com/chromium/src/?format=JSON` on curl 8.21.0, Windows; run 2026-09-26
- **Set by:** none
- **Method:** `python -B gate/run_tests.py elements/environment-facts/probes/chromium-src-visibility --record .runs/fact-chromium-src-visibility.jsonl`
- **Correction:** none

## Withdrawn identifiers

| Identifier | Why | Successors |
|---|---|---|
