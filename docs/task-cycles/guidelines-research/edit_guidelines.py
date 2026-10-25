from pathlib import Path
import re

ROOT = Path('C:/Storage/repos/the-way-wt/guidelines-research')

def read(path):
    return (ROOT / path).read_bytes().decode('utf-8')

def write(path, text):
    (ROOT / path).write_bytes(text.encode('utf-8'))

def replace(text, old, new):
    if text.count(old) != 1:
        raise ValueError(f'Expected one match: {old[:80]!r}; got {text.count(old)}')
    return text.replace(old, new)

path = 'foundations/decisions.md'
text = read(path)
newline = '\r\n' if '\r\n' in text else '\n'
text = text.replace('\r\n', '\n')

def entry(number):
    return re.search(rf'^### WAY-{number} .*?(?=^### WAY-|^## Withdrawn|\Z)', text, re.M | re.S).group()

def update(number, changes):
    global text
    old = entry(number)
    new = old
    for before, after in changes:
        new = replace(new, before, after)
    text = replace(text, old, new)

recommendation = '''showing the options by their consequences for the product — cost, where they run,
upkeep and the cost of changing later — with a recommendation and the weak point of the option
recommended, and recommending the simplest and cheapest where no difference with a consequence
remains (WAY-123)'''

update(185, [
    ('styling is a choice the skill leaves to the human as a question of the task, never one it settles. A\npalette',
     'styling is a choice the skill leaves to the human as a question of the task, never one it settles,\n' + recommendation + '. A palette'),
    ('- **Relations:** none', '- **Relations:** derives from WAY-121 · derives from WAY-123'),
    ('    to the human;', '    to the human with consequences, a recommendation and its weak point;'),
    ('    the skill chooses a styling technology itself; the colours the code uses become a rule of the',
     '    the skill chooses a styling technology itself or offers options without a recommendation;\n    the colours the code uses become a rule of the'),
    ('something the product has to keep, a technology choice, and the human makes it.',
     'something the product has to keep, a technology choice, and the human makes it. A human who\ncannot judge the library can weigh what it costs and where it fails; the recommendation gives a\nway to take without deciding by technical names alone.'),
    ('palette the code uses taken as the product\'s rule — an accident of the code becomes law (WAY-225).',
     'palette the code uses taken as the product\'s rule — an accident of the code becomes law (WAY-225);\noptions with no recommendation — the human is left to judge technology they cannot assess.')
])

update(210, [
    ("task, never one it settles, recommending by default the tool most used in the product's technology,\nas research with sources shows it.",
     'task, never one it settles, ' + recommendation + '.'),
    ('- **Relations:** derives from WAY-173', '- **Relations:** derives from WAY-173 · derives from WAY-121 · derives from WAY-123'),
    ("    recommending the tool research shows most used in the product's technology, with its sources;",
     '    showing the consequences with a recommendation and its weak point, and recommending the\n    simplest and cheapest where no difference with a consequence remains;'),
    ("    better; the skill chooses a formatter itself; the default recommendation is a tool the agent\n    prefers, with no source showing its use.",
     '    better; the skill chooses a formatter itself; a tool is recommended only because it is the\n    most used, although another has better consequences for the product.'),
    ('a technology choice, and the human makes it. The human is no developer, and a product with no\nstanding check meets three such choices at once, so the skill recommends the tool most used in the\ntechnology, which the human can take as offered, as WCAG is recommended for adoption (WAY-191), and\nhow widely an option is used within its family bears on how well an agent works with it (WAY-122).',
     'a technology choice, and the human makes it. The human is no developer, so a recommendation\nthrough consequences gives a way they can weigh and take as offered, with its weakness visible.\nWide use can bear on those consequences (WAY-122), but cannot replace them.'),
    ('never chose.', 'never chose; the most-used tool as the default recommendation — popularity alone says nothing\nof whether the product benefits; options with no recommendation — the human is left to judge\ntechnology they cannot assess.')
])

update(248, [
    ('a question of the task, never one it settles.',
     'a question of the task, never one it settles, ' + recommendation + '.'),
    ('- **Relations:** derives from WAY-173 · derives from WAY-121',
     '- **Relations:** derives from WAY-173 · derives from WAY-121 · derives from WAY-123'),
    ('    gets the choice of that library as a question of the task;',
     '    gets the choice of that library as a question of the task, with consequences, a\n    recommendation and its weak point;'),
    ('    better; the skill adds a library of property tests itself.',
     '    better; the skill adds a library of property tests itself or leaves its choice to the human\n    with no recommendation.'),
    ('to keep, a technology choice, and the human makes it (WAY-121).',
     'to keep, a technology choice, and the human makes it (WAY-121). A human who cannot judge test\ntools can weigh consequences and take a recommendation with its weakness visible.'),
    ('the skill choosing a new tool itself — a dependency the human never chose.',
     'the skill choosing a new tool itself — a dependency the human never chose; options with no\nrecommendation — the human is left to judge technology they cannot assess.')
])

update(186, [
    ('''The skill `maintain-styleguide` takes the starting rules of a styleguide written before the first
screen of its user interface from the human's preferences for the technology of that user interface
that the product's foundation settles, and, where the human has none, from research of the basic rules of a styleguide for that technology, each source named with
its page and version and every difference no source supports refuted by a critique before the human
sees the rules, as the options of a technology choice are checked (WAY-122). It adds the meanings of
the screens the product announces — in its definition, plan, specs and mockups — proposes what the
research finds without imposing it, and researches again whenever a styleguide is refreshed or
extended.''',
     '''The skill `maintain-styleguide` takes the starting rules of a user interface's first styleguide
from the human's preferences for its technology that the product's foundation settles, and, where
the human has none, from research of the basic rules for that technology, each source named with its
page and version and every difference no source supports refuted by a critique before the human
sees the rules, as the options of a technology choice are checked (WAY-122). It researches at every
extension and never at a refresh (WAY-251), and a tool the human prefers remains the one proposed,
never displaced by research. It adds the meanings of the screens the product announces — in its
definition, plan, specs and mockups — and proposes what the research finds without imposing it.'''),
    ('- **Relations:** derives from WAY-122 · derives from WAY-120',
     '- **Relations:** derives from WAY-122 · derives from WAY-120 · derives from WAY-251'),
    ('''    gives, and the starting set adds roles for the states the game's plan announces; a year later an
    extension runs the research again; a product that has screens and no styleguide starts from the
    audit of its code, with no research until its styleguide is refreshed or extended;''',
     '''    gives, and the starting set adds roles for the states the game's plan announces; a product
    with screens and no styleguide takes that same starting-set path alongside its audit; an
    extension runs research with the human's preferred tool kept as the proposal; a correction of
    existing roles refreshes the styleguide without research;'''),
    ('''    is used for every product; research reaches the human uncritiqued; an extension reuses the
    first research.''',
     '''    is used for every product; research reaches the human uncritiqued; an extension reuses the
    first research; a refresh runs research; research offers another tool in place of the human's
    preferred one.'''),
    ('''product's own meanings one colour comes back in several meanings. Recommendations move, so a
refreshed styleguide is set against them again. A product that already has screens starts from what
its code holds, which the audit reads (WAY-187), so its first styleguide needs no starting set.''',
     '''product's own meanings one colour comes back in several meanings. New scope needs a check of
whether the existing tools fit it, while correcting accepted rules within their scope needs no new
comparison. Existing screens supply audit evidence, not preferences or a reason to skip research
where the human has none.'''),
    ('one.\n\n', 'one; research at every refresh — an update within accepted scope pays for a comparison it does\nnot need.\n\n')
])

update(211, [
    ('''settles, and, where the human has none, from research of each standing check for that technology,''',
     '''settles, and, for the first coding guidelines where the human has none, from research of each
standing check for that technology,'''),
    ('''before the human sees the options, as the options of a technology choice are checked (WAY-122). It
researches again whenever a product's coding guidelines are refreshed or extended.''',
     '''before the human sees the options, as the options of a technology choice are checked (WAY-122).
A tool the human prefers remains the one proposed, never displaced by research. The skill
researches at every extension and never at a refresh (WAY-251).'''),
    ('- **Relations:** derives from WAY-122 · derives from WAY-120',
     '- **Relations:** derives from WAY-122 · derives from WAY-120 · derives from WAY-251'),
    ('''    options; a year later an extension of the coding guidelines runs the research again;''',
     '''    options; an extension runs research with the human's preferred tool kept as the proposal;
    adapting the existing guidelines to a new tool version refreshes them without research;'''),
    ('''    extension reuses the first research; the skill researches a tool the human already named as
    preferred and offers another in its place.''',
     '''    extension reuses the first research; a refresh runs research; the skill offers another tool
    in place of one the human named as preferred.'''),
    ('''from an invented one (WAY-122, WAY-120), as for a styleguide's starting rules (WAY-186). Tools and
their recommended sets move, so refreshed coding guidelines are set against them again.''',
     '''from an invented one (WAY-122, WAY-120), as for a styleguide's starting rules (WAY-186). New
scope needs a check of whether the existing tools fit it, while updating or correcting accepted
rules within their scope needs no new comparison.'''),
    ('from an invented one; research once for each product — later extensions miss what has moved.',
     'from an invented one; research once for each product — later extensions miss what has moved;\nresearch at every refresh — an update within accepted scope pays for a comparison it does not need.')
])

update(249, [
    ("from the human's preferences, and, where the human has none, from research for the product's",
     "from the human's preferences, and, for its first testing guidelines where the human has none,\nfrom research for the product's"),
    ('''options of a technology choice are checked (WAY-122). It proposes what the research finds without
imposing it.''',
     '''options of a technology choice are checked (WAY-122). It researches at every extension and never
at a refresh (WAY-251), and a tool the human prefers remains the one proposed, never displaced by
research. It proposes what the research finds without imposing it.'''),
    ('- **Relations:** derives from WAY-173 · derives from WAY-122 · derives from WAY-120',
     '- **Relations:** derives from WAY-173 · derives from WAY-122 · derives from WAY-120 ·\n  derives from WAY-251'),
    ('    human sees the set;',
     '    human sees the set; an extension to a new test level runs research, keeping the human\'s\n    preferred tool as the proposal; correcting the existing recipes refreshes them without research;'),
    ('    task as settled.',
     '    task as settled; an extension reuses the first research; a refresh runs research; research\n    offers another tool in place of the human\'s preferred one.'),
    ('question keeps each research to its question and its report.',
     'question keeps each research to its question and its report. New scope needs a check of whether\nthe existing tools fit it, while updating or correcting accepted recipes within their scope needs\nno new comparison.'),
    ('technology.\n\n',
     'technology; research once for each product — later extensions miss what has moved; research at\nevery refresh — an update within accepted scope pays for a comparison it does not need.\n\n')
])

new_entry = '''### WAY-251 — What distinguishes a refresh from an extension of guidelines?

For the skills `maintain-coding-guidelines`, `maintain-styleguide` and
`maintain-testing-guidelines`, a refresh updates or corrects accepted guidelines within the scope
they already cover, including adapting them to a new version of a tool the product already uses.
An extension covers something new, and its research checks whether to use what the product already
has or something else, with the human's preferred tool remaining the proposal.

- **Scope:** product-guidelines
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the work with the decision:
  - complies: adapting the accepted testing guidelines to a new major version of their test tool
    is a refresh; covering a new level of tests is an extension whose research checks whether the
    product's existing tool fits it;
  - violates: a change of a tool's version alone is treated as an extension; a new scope is called
    a refresh merely because the product already has a tool that might serve it.
- **Origin:** none

*Rationale:* an update within accepted scope corrects guidance for something the product already
does; a new scope raises whether the existing tools suit it. Telling them apart by scope gives every
discipline the same boundary and spends research where it answers a new question. A preference
still belongs to the human, so research informs its use rather than replacing it.
*Rejected:* refresh and extension treated alike — routine corrections pay for research, or new
scope receives none; a version change alone treated as an extension — new versions can leave the
covered scope unchanged.

'''
text = replace(text, '## Withdrawn identifiers\n', new_entry + '## Withdrawn identifiers\n')
write(path, text.replace('\n', newline))

for discipline, decision in [('coding', '211'), ('styleguide', '186'), ('testing', '249')]:
    path = f'product-guidelines/{discipline}/SKILL.md'
    text = read(path)
    newline = '\r\n' if '\r\n' in text else '\n'
    text = text.replace('\r\n', '\n')
    text = replace(text, '## 2. Starting ' + ('rules' if discipline == 'styleguide' else 'set'),
                   '''A refresh updates or corrects accepted guidelines within the scope they already cover,
including adapting them to a new version of a tool the product uses. An extension covers something
new; its research checks whether to use what the product has or something else (WAY-251).

## 2. Starting ''' + ('rules' if discipline == 'styleguide' else 'set'))
    text = replace(text, '- Give one fresh agent, following `critique`, each report with its sources,',
                   '- Where research ran, give one fresh agent, following `critique`, each report with its sources,')
    text = text.replace("the research's sources, each page with its version;", "the research's sources where research ran, each page with its version;")
    text = text.replace('and the\n  research reports as its source,', 'and any\n  research reports as its source,')
    text = text.replace('the\n  research and trial-run reports as its source,', 'any\n  research reports and the trial-run reports as its source,')
    choice_decision = {'coding': '210', 'styleguide': '185', 'testing': '248'}[discipline]
    tool_choice = '''- **New tools.** For each new tool or library left as a technology question of the task,
  show the options by their consequences for the product: cost, where they run, upkeep and the
  cost of changing later. Give a recommendation and the weak point of the option recommended;
  where no difference with a consequence remains, recommend the simplest and cheapest. Keep the
  human's preferred tool as the proposal, and leave the choice to the human in this task
  (WAY-''' + choice_decision + ', WAY-' + decision + ''', WAY-123, WAY-121).
'''
    text = replace(text, '- **What it settles.**', tool_choice + '- **What it settles.**')
    if discipline == 'coding':
        text = replace(text, '''- Where the human has none, and at every refresh or extension, research each standing check for
  that technology, giving each to a fresh agent of its own, all at once, with the technology, the
  preferences and the binding sentences of the decisions that settle it: the tools used for it,
  which of them is most used in that technology — the default recommendation (WAY-210) — the sets
  of rules a linter offers with the rules its documentation marks as recommended, and the advisory
  databases an audit reads.''', '''- For the first coding guidelines where the human has no preference, and at every extension,
  research each standing check for that technology; at a refresh, do no research and use the
  accepted guidelines with the update or correction the task calls for. Give each research question
  to a fresh agent of its own, all at once, with the technology, the preferences, the scope being
  added where this is an extension, and the binding sentences of the decisions that settle it:
  the tools and their consequences for the product, the sets of rules a linter offers with the
  rules its documentation marks as recommended, and the advisory databases an audit reads.''')
        text = replace(text, '''  marks as recommended, as the research reads them: there is no code to try them on (WAY-204).''',
                       '''  marks as recommended: read that documentation at the proposed version also where preferences
  supplied the tool and no research ran; there is no code to try them on (WAY-204).''')
        text = replace(text, '''- **Trial run** (WAY-204). Run the linter's set — the one the product runs with the rules the
  research of step 2 proposes adding, or the one step 2 proposes — at the version the research or
  the product's files give,''', '''- **Trial run** (WAY-204). Run the linter's set — the one the product runs with the additions or
  corrections step 2 proposes, or the one step 2 proposes from preferences or research — at the
  version read from the product's files or the proposed tool's documentation,''')
    elif discipline == 'styleguide':
        text = replace(text, '''  audit of step 3; an existing styleguide, its refresh or extension — step 2, and step 3 where''',
                       '''  starting rules of step 2 and the audit of step 3; an existing styleguide, its refresh or
  extension — step 2, and step 3 where''')
        text = replace(text, 'Before the first screen, and at every refresh or extension (WAY-184, WAY-186):',
                       'For the first styleguide, with or without screens, and at every refresh or extension\n(WAY-184, WAY-186):')
        text = replace(text, '''  the user interface that the product's foundation settles; "I do not know" is an answer.''',
                       '''  the user interface that the product's foundation settles; "I do not know" is an answer.
  A tool the human prefers is the one proposed, and no other is offered in its place (WAY-186).''')
        text = replace(text, '''- Where the human has none, and at every refresh or extension, research the basic rules of a
  styleguide for that technology. Split it into the questions the starting set must answer there —''',
                       '''- For the first styleguide where the human has no preference, and at every extension, research
  the basic rules for that technology; at a refresh, do no research and use the accepted
  styleguide with the update or correction the task calls for. Split research into the questions
  the starting set or the scope being added must answer there —''')
        text = replace(text, '''  preferences and the binding sentences of the decisions that settle it. Each source''',
                       '''  preferences, the scope being added where this is an extension, and the binding sentences of
  the decisions that settle it. Include any new tool's consequences for the product. Each source''')
    else:
        text = replace(text, '''  what a test replaces and with what; "I do not know" is an answer.''',
                       '''  what a test replaces and with what; "I do not know" is an answer. A tool the human prefers is
  the one proposed, and no other is offered in its place (WAY-249).''')
        text = replace(text, '''- Where the human has none, research the starting set for that technology. Split it into the
  questions the set must answer there —''',
                       '''- For the first testing guidelines where the human has no preference, and at every extension,
  research the set for that technology; at a refresh, do no research and use the accepted guidelines
  with the update or correction the task calls for. Split research into the questions the starting
  set or the scope being added must answer there —''')
        text = replace(text, '''  the preferences and the binding sentences of the decisions that settle it. Each source is a page''',
                       '''  the preferences, the scope being added where this is an extension, and the binding sentences
  of the decisions that settle it. Include any new tool's consequences for the product. Each source is a page''')
    write(path, text.replace('\n', newline))

print('Updated 4 files')
