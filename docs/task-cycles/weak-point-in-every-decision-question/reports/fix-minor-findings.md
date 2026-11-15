# Findings to fix — Minor findings of the review of the whole change

Cut word for word from `reports/review-whole-report.md` (PASS a3c97dff32f5341cee667eaa2619a18d96b1bdc3), section "Minor (all within the task)". No blocking finding. Fix each in one fix; the reviewer marked none outside the task.

1. `process-audit/SKILL.md:155-156` — the step reads the newest earlier note "only to see which matters the human weighed or
   set aside; say so beside a matter that comes again". The change adds a third outcome and a field *Decided* to the
   note (`:11-14`, `:261-263`) but this sentence still names two. A matter decided in an earlier session therefore comes
   again with no remark beside it, which the sentence is there to prevent. Fix: add "decided on a step" there. Why it
   matters: the audit would put a decided matter before the human as new. Evidence: grep for "set aside" in
   `process-audit/SKILL.md` gives lines 13, 156, 169, 261-264; only 155-156 was not updated.
2. `task-cycle/skill/request_template.md:424` (and `:400-402`) — the example items say "undoing it, nothing" for
   every way, including "Letting it through accepts that risk; undoing it, nothing" in an item whose own first
   sentences say the user "loses the change on the first day". The rule's purpose is to name the choice that cannot be
   taken back cheaply; the example shows the word on every way and thereby teaches writing it by rote, and for that
   way it is arguably untrue. Fix: let one way in an example carry a real cost of undoing (for instance the way that
   accepts the risk: "undoing it, a correction after users lose data"). Examples carry no binding force; the
   consequence I name is the copying of the rote word. Within the task (*To do* 3: the examples show it).
3. `foundations/decisions.md` WAY-113 *Verification*, `complies` (the line on "the rounds of a project definition"): it
   gives only an example of the implication move. The binding sentence, *violates* and the task (*To do* 6: "Verification
   uznaje takie pytanie przy definicji za zgodne") name both moves, the implication and the reason of a decision costly
   to reverse. A reader comparing an exchange where the reason of a costly decision is asked in the rounds finds no
   `complies` case for it. Fix: add the reason move to that line.
4. `project-level/skill/rounds.md:8-18` — (a) the list is headed "Four moves", though its fourth item ("I do not know")
   is a rule for an answer, which the author notes; (b) that item's text changed from "to a question of decision, give a
   recommendation, with what each way costs" to "ask as 'How a skill asks' gives a question of decision". The old
   instruction was what to do when the human says "I do not know" — give a recommendation; the new one says "ask", which
   a reader can take as asking the same question again. Fix: "to a question of decision, answer with a recommendation put
   as 'How a skill asks' gives it" and a heading that says "Two moves ... and one rule" or similar.
5. Wrapping leftovers after the rewording, cosmetic: `foundations/decisions.md` WAY-378 binding sentence (line "plain language
   as WAY-113 asks a decision; the" is short, then "full list and the critique"), WAY-174 *Verification* ("as a question of
   decision (WAY-113); it asks" short lines), and `project-level/lead/skill/route_changes.md:17-19` (a line of 106 characters
   where the file wraps at 100). No reader is misled.
