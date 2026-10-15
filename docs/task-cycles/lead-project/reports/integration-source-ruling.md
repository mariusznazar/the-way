
## Integration-source clarification

A working branch's upstream is not a declaration of the product integration branch. The installed product guidance already declares `origin/HEAD`: installation/install.py product_guidance(), lines158-166, says `git symbolic-ref --short refs/remotes/origin/HEAD` names it as `origin/<branch>` and otherwise asks the human. Use that existing origin route, confirmed through Git; another configured remote with a different default does not by itself make a valid origin route ambiguous. No main/master fallback or inference from the checked-out/upstream branch.

For the ambiguous case, origin metadata that cannot establish one valid default route remains unchecked. Do not commit a negative expectation that rejects origin merely because another remote exists; instead exercise the presence of another remote as a positive no-false-ambiguity case, preserving origin's completion evidence. A missing/invalid origin default remains the existing negative case. No configuration or new CLI override is added in this task. This is source-grounded observability clarification, not a code algorithm handed to the check author.
