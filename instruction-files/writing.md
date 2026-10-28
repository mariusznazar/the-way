# Writing the instruction files of a repository that has none

How the skill writes them, in the mode write.

The rules of an instruction file cannot be derived from the repository; the repository gives at
most a check of what the human says.

1. From the repository take only what meets the three conditions of "Where a rule stands" —
   typically a command the agent would not guess.
2. Ask the human for the rest — the kinds of content the main file holds. Leave `TODO` where there
   is no answer; do not fill it from the code.
3. Lay the files out by "One layout for three tools" and the file of their kind, for the tools in
   use.
4. Name the file's sections in the words its readers use for the product, such as `Where things
   are`, `Before you release`, `Rules`, written in the language of the repository.
5. Show the files and write them only after approval.
