# Reviewing a spec

What the reviewer of a spec, or of its revision, reports and returns.

## Review a spec

As the reviewer, read the spec as the agent who has to plan and build from it without talking to
its author, against the frozen task and the foundation entries the dispatch names. Report only
what would make the build go wrong:

- a requirement of the task the spec drops or changes;
- behaviour the spec invents that the task does not ask for;
- a contradiction with the task, the foundation or itself;
- a place where the builder would have to guess and a wrong guess would matter — the question and
  why the answer changes the build.

Skip wording, style and what the spec leaves to the maker. The first line of your report is
`PASS` or `FAIL`; `FAIL` means at least one finding of the list above. For the review of a revised
spec, say for each earlier finding whether it is resolved, and report only what the revision
broke besides.

## Return

The reviewer writes its report, each reach included, to its own path and returns its first line.
