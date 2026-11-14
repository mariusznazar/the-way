p = 'foundations/decisions.md'
t = open(p, encoding='utf-8', newline='').read()


def rep(old, new):
    global t
    assert t.count(old) == 1, (t.count(old), old[:80])
    t = t.replace(old, new)


# WAY-276
rep("quotes such values this rule prevails over WAY-272, and the error is written without them, with its\nkind, code and place in the code;",
    "quotes such values this rule prevails over the rule that a failure is written with its original error,\nand the error is written without them, with its kind, code and place in the code;")
rep("this rule prevailing over WAY-275. The ban", "this rule prevailing over the rule that a line of a case flow carries the identifiers the\nlogging scope lists. The ban")
rep("apart from it (WAY-86). Where an error quotes", "apart from it. Where an error quotes")
# WAY-280
rep("stand in one\norder (WAY-282). Many small breaks", "stand in one\norder. Many small breaks")
# WAY-284
rep("causes of the top of an audit's\nlist (WAY-283) a task takes", "causes of the top of an audit's\nlist a task takes")
rep("the list the limit took\naway (WAY-283). Its weak point", "the list the limit took\naway. Its weak point")
# WAY-287
rep("""holds wrong (WAY-295), an
error of the form check that the cycle holds wrong (WAY-291), the pairs that give the cause of a
correction after the request opened (WAY-358), each descriptive""", """holds wrong (WAY-295), an
error of the form check that the cycle holds wrong, the pairs that give the cause of a
correction after the request opened, each descriptive""")
rep("it changes the skeleton of WAY-286 and every reference", "it changes the skeleton of the request's description and every reference")
# WAY-300
rep("since the last\nreview tag (WAY-301), and from 30 merges", "since the last\nreview tag, and from 30 merges")
# WAY-315
rep("for the rows of its settlements (WAY-115, WAY-134)", "for the rows of its settlements (WAY-134)")
# WAY-316: WAY-219 is the author's check of a user-interface change
rep("the author inspects the screenshot as WAY-219 gives and the request shows none:", "the author inspects the screenshot as the author's check of a user-interface change gives and the\nrequest shows none:")
rep("product is reported as WAY-219 gives and needs no second item.", "product is reported as that check gives and needs no second item.")
rep("    WAY-219 gives, with no item about a place;", "    that check gives, with no item about a place;")
rep("""WAY-219 refused to stop the cycle for an unsettled way to the interface, and the same holds here: a
stop comes after the change is made, when it can no longer be avoided. The case differs from that of
WAY-219: there the author cannot look at the screen, here it looks and has nowhere to put the result.""", """The author's check of a user-interface change refused to stop the cycle for an unsettled way to the
interface, and the same holds here: a stop comes after the change is made, when it can no longer be
avoided. The case differs from that of an unsettled way: there the author cannot look at the screen,
here it looks and has nowhere to put the result.""")
rep("the stop comes after the change is made, which\nWAY-219 refused for the way to the product.", "the stop comes after the change is made, which\nthe author's check of a user-interface change refused for the way to the product.")
# WAY-328
rep("testing guidelines of a product, under WAY-217: in each part", "testing guidelines of a product, under the shared reading of product guidelines: in each part")
# WAY-339
rep("the prompt cache (WAY-347) and the times of the gate (WAY-349): a new", "the prompt cache and the times of the gate: a new")
rep("the tables of WAY-349 and WAY-350 and the", "the tables of the gate times and of WAY-350 and the")
# WAY-360
rep("as WAY-278 gives it for the rules on failures and\nlogs.", "as the skill `maintain-coding-guidelines` gives it for the rules on failures and\nlogs.")
rep("takes the proposal up (WAY-202); required, the rule", "takes the proposal up; required, the rule")
rep("does not read as an oversight (WAY-278). The price", "does not read as an oversight. The price")
rep("takes the proposal up (WAY-202); no rule in the template", "takes the proposal up; no rule in the template")
open(p,'w',encoding='utf-8',newline='').write(t)
print('ok')
