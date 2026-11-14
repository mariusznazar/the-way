p = 'foundations/decisions.md'
t = open(p, encoding='utf-8', newline='').read()


def rep(old, new):
    global t
    assert t.count(old) == 1, (t.count(old), old[:80])
    t = t.replace(old, new)


# ---- relations to a withdrawn number: the relation goes
rep("- **Based on:** git-path-patterns\n- **Relations:** derives from WAY-40\n", "- **Based on:** git-path-patterns\n- **Relations:** none\n")  # WAY-44
rep("- **Scope:** part-map, task-cycle\n- **Based on:** none\n- **Relations:** derives from WAY-40\n", "- **Scope:** part-map, task-cycle\n- **Based on:** none\n- **Relations:** none\n")  # WAY-48
rep("- **Relations:** derives from WAY-40 · derives from WAY-21 · derives from WAY-44\n", "- **Relations:** derives from WAY-21 · derives from WAY-44\n")  # WAY-52
rep("- **Relations:** derives from WAY-22 · derives from WAY-56\n", "- **Relations:** derives from WAY-22\n")  # WAY-60
rep("- **Relations:** derives from WAY-226 · narrows WAY-99\n", "- **Relations:** narrows WAY-99\n")  # WAY-104
rep("- **Relations:** derives from WAY-106 · derives from WAY-116 · derives from\n  WAY-100\n", "- **Relations:** derives from WAY-106 · derives from WAY-100\n")  # WAY-121
rep("- **Relations:** derives from WAY-115 · derives from WAY-33 · narrows WAY-114\n", "- **Relations:** derives from WAY-33 · narrows WAY-114\n")  # WAY-134
rep("- **Relations:** derives from WAY-202 · derives from WAY-100\n- **Verification:** an agent compares the work with the decision:\n  - complies: a rule on unused variables", "- **Relations:** derives from WAY-100\n- **Verification:** an agent compares the work with the decision:\n  - complies: a rule on unused variables")  # WAY-203
rep("- **Relations:** derives from WAY-202 · derives from WAY-60 · derives from WAY-100\n", "- **Relations:** derives from WAY-60 · derives from WAY-100\n")  # WAY-206
rep("- **Relations:** derives from WAY-167 · derives from WAY-171 · derives from\n  WAY-150 · derives from WAY-36\n", "- **Relations:** derives from WAY-167 · derives from WAY-150 · derives from WAY-36\n")  # WAY-213
rep("""- **Relations:** derives from WAY-124 · derives from WAY-144 · derives from
  WAY-154 · derives from WAY-172 · derives from WAY-199 · derives from
  WAY-184 · derives from WAY-209 · derives from WAY-217 · derives from
  WAY-244
""", """- **Relations:** derives from WAY-124 · derives from WAY-144 · derives from
  WAY-154 · derives from WAY-172 · derives from WAY-199 · derives from
  WAY-244
""")  # WAY-215
rep("- **Relations:** derives from WAY-200 · derives from WAY-209 · narrows WAY-251 · narrows WAY-202\n", "- **Relations:** narrows WAY-251\n")  # WAY-216
rep("- **Relations:** derives from WAY-173 · derives from WAY-226 · narrows WAY-95\n", "- **Relations:** derives from WAY-173 · narrows WAY-95\n")  # WAY-240
rep("- **Relations:** derives from WAY-173 · derives from WAY-200 · derives from WAY-172\n", "- **Relations:** derives from WAY-173 · derives from WAY-172\n")  # WAY-242
rep("- **Relations:** derives from WAY-173 · derives from WAY-68 · derives from WAY-233\n", "- **Relations:** derives from WAY-173 · derives from WAY-233\n")  # WAY-243
rep("- **Relations:** derives from WAY-271 · derives from WAY-100\n- **Verification:** an agent compares the template with the decision:\n  - complies: the rule has a list whose source failed", "- **Relations:** derives from WAY-100\n- **Verification:** an agent compares the template with the decision:\n  - complies: the rule has a list whose source failed")  # WAY-273
rep("- **Relations:** derives from WAY-271 · derives from WAY-172 · derives from WAY-225\n", "- **Relations:** derives from WAY-172 · derives from WAY-225\n")  # WAY-274
rep("- **Relations:** derives from WAY-271 · derives from WAY-86 · narrows WAY-272 · narrows WAY-275\n", "- **Relations:** none\n")  # WAY-276
rep("- **Relations:** derives from WAY-283 · derives from WAY-174 · derives from WAY-215\n", "- **Relations:** derives from WAY-174 · derives from WAY-215\n")  # WAY-284
rep("- **Relations:** derives from WAY-227 · derives from WAY-286\n", "- **Relations:** derives from WAY-227\n")  # WAY-287
rep("- **Relations:** derives from WAY-286 · narrows WAY-114\n", "- **Relations:** narrows WAY-114\n")  # WAY-288
rep("""- **Relations:** derives from WAY-219 · derives from WAY-286 · derives from WAY-308 · derives from
  WAY-287
""", """- **Relations:** derives from WAY-308 · derives from WAY-287
""")  # WAY-316
rep("- **Relations:** derives from WAY-121 · derives from WAY-219\n", "- **Relations:** derives from WAY-121\n")  # WAY-319
rep("- **Relations:** derives from WAY-217 · derives from WAY-173\n", "- **Relations:** derives from WAY-173\n")  # WAY-328
rep("- **Relations:** derives from WAY-349\n", "- **Relations:** none\n")  # WAY-350
rep("""- **Relations:** derives from WAY-140 · derives from WAY-153 · derives from WAY-298 ·
  derives from WAY-373
""", """- **Relations:** derives from WAY-140 · derives from WAY-153 · derives from WAY-373
""")  # WAY-375

# ---- WAY-09, WAY-312, WAY-93 and the other references in text
rep("in a directory of their own (WAY-331).", "in a directory of their own.")  # WAY-09 rationale
rep("an omitted field looks forgotten (WAY-58); an undefined", "an omitted field looks forgotten; an undefined")  # WAY-71
rep("shown, or, where no page open to a reader shows it, a reading (WAY-80). A choice", "shown, or, where no page open to a reader shows it, a reading. A choice")  # WAY-84
rep("what a reader with access compares with it (WAY-80).\n", "what a reader with access compares with it.\n")  # WAY-84
rep("fact entry needs a source a reader can open (WAY-80) while no entry", "fact entry needs a source a reader can open while no entry")  # WAY-90
rep("fact would name at a fixed commit — a new form of source beside those of WAY-80, a new kind of file", "fact would name at a fixed commit — a new form of source beside those an environment fact takes, a new kind of file")  # WAY-90
rep("*Rejected:* terms in the shared space of identifiers (WAY-64) — a word", "*Rejected:* terms in the shared space of identifiers — a word")  # WAY-93
rep("""the choice standing: only the behaviour when no place for
screenshots is settled (WAY-317)""", """x""") if False else None
rep("screenshots is settled (WAY-317), with the step unchanged", "screenshots is settled (WAY-316), with the step unchanged")  # WAY-121
rep("moves a fragment beside a skill asks whether an agent recognises that moment (WAY-257).", "moves a fragment beside a skill asks whether an agent recognises that moment.")  # WAY-125
rep("the lines of process skills and their entry points answer to WAY-35, WAY-127, WAY-256 and WAY-259\ninstead.", "the lines of process skills and their entry points answer to WAY-35, WAY-127 and WAY-256, and to the\ntext the installer writes in an entry point, instead.")  # WAY-128
rep("document and the conversation that refined it, in the form WAY-115 gives with each settlement in\nthe human's words", "document and the conversation that refined it, in the form of the candidate table of the skills of the\nelements (`elements/common/skill/build_table.md`) with each settlement in\nthe human's words")  # WAY-134
rep("the definition holds it (WAY-110); the columns named in this", "the definition holds it; the columns named in this")  # WAY-142
rep("brings the rule in line (WAY-169). A rule that only says how to", "brings the rule in line. A rule that only says how to")  # WAY-168
rep("decision adopting the set (WAY-207), put to a human who does not judge code;", "decision adopting the set, put to a human who does not judge code;")  # WAY-203
rep("one reason to change, a new edition (WAY-76), as\ngit's rule", "one reason to change, a new edition, as\ngit's rule")  # WAY-204
rep("fact of its own (WAY-191) because each is a requirement", "fact of its own because each is a requirement")  # WAY-204
rep("one source and one reason to change (WAY-76).\n", "one source and one reason to change.\n")  # WAY-204
rep("such\na check is answered as WAY-68 gives it, which this decision leaves unchanged.", "such\na check is answered as any check that gives different verdicts on one commit is, by a fix of the test with no\nquarantine recorded, which this decision leaves unchanged.")  # WAY-206
rep("WAY-68 narrowed so that a later `fail` on the same commit is no check giving different verdicts — a\nnew meaning of WAY-68 for a rare case;", "the rule on a check that gives different verdicts on one commit narrowed so that a later `fail` on the\nsame commit is no such check — a new meaning of that rule for a rare case;")  # WAY-206
rep("a kind's file catches (WAY-170). The pointer", "a kind's file catches. The pointer")  # WAY-212
rep("for each file of the coding guidelines, as WAY-192 has for each\nstyleguide —", "for each file of the coding guidelines, as it has for each\nstyleguide —")  # WAY-212
rep("Unless a departure under WAY-217 applies, a task", "Unless an approved departure under the shared reading of product guidelines applies, a task")  # WAY-215
rep("gains in *To do* the designation of that kind's exemplar under WAY-200 and its kind guidelines", "gains in *To do* the designation of that kind's exemplar as the skill `maintain-coding-guidelines` gives it and its kind guidelines")  # WAY-216
rep("selection through the comparison WAY-200 gives existing code, rather than", "selection through the comparison that skill gives existing code, rather than")  # WAY-216
rep("is no audit under WAY-201.", "is no audit of a product with code.")  # WAY-216
rep("keeps its research (WAY-211). In a product", "keeps its research. In a product")  # WAY-216
rep("each standing check already stands decided (WAY-202), so a kind", "each standing check already stands decided, so a kind")  # WAY-216
rep("extension for another reason, against WAY-211; only the checks", "extension for another reason, against the rule that an extension researches; only the checks")  # WAY-216
rep("which an agent reads before it writes or changes\na test (WAY-246). A property", "which an agent reads before it writes or changes\na test. A property")  # WAY-228
rep("it takes the same cause and evidence. WAY-68\ngives the test of an invariant the same answer.", "it takes the same cause and evidence. The rule on a check that gives different verdicts on one commit\ngives the test of an invariant the same answer.")  # WAY-243
rep("which ages, as WAY-68 refuses it for the tests of invariants;", "which ages, as that rule refuses it for the tests of invariants;")  # WAY-243
rep("every later screen copies (WAY-184), and guidelines brought to", "every later screen copies, and guidelines brought to")  # WAY-244
rep("both before its first code (WAY-209, WAY-244), and two tasks", "both before its first code (WAY-244), and two tasks")  # WAY-247
rep("the check of the plan again (WAY-118, WAY-156), and an independent", "the check of the plan again (WAY-118), and an independent")  # WAY-267
rep("alone stops no cycle (WAY-219); a new linter", "alone stops no cycle; a new linter")  # WAY-268
rep("skills and the decisions on their routes (WAY-185, WAY-186, WAY-210, WAY-211, WAY-248, WAY-249)\nwould have to change,", "skills and the decisions on their routes\nwould have to change,")  # WAY-268
rep("where an error\nquotes such values this rule prevails over WAY-272, and the error", "where an error\nquotes such values this rule prevails over the rule that a failure is written with its original error, and the error") if False else None
open(p, 'w', encoding='utf-8', newline='').write(t)
print('part 1 ok')
