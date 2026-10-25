from pathlib import Path
import re
import textwrap

root = Path('C:/Storage/repos/the-way-wt/guidelines-research')
for relative in ['foundations/decisions.md', *[f'product-guidelines/{kind}/SKILL.md' for kind in ('coding', 'styleguide', 'testing')]]:
    path = root / relative
    raw = path.read_bytes().decode('utf-8')
    newline = '\r\n' if '\r\n' in raw else '\n'
    text = raw.replace('\r\n', '\n')
    if relative.startswith('foundations'):
        for number, preference in [(185, 186), (210, 211), (248, 249)]:
            pattern = rf'^### WAY-{number} .*?(?=^### WAY-|^## Withdrawn|\Z)'
            match = re.search(pattern, text, re.M | re.S)
            old = match.group()
            new = old.replace('recommended, and recommending the simplest and cheapest where no difference with a consequence\nremains (WAY-123).',
                              f'recommended, keeping the human\'s preferred tool as the recommendation (WAY-{preference}) and\notherwise recommending the simplest and cheapest where no difference with a consequence remains\n(WAY-123).')
            text = text.replace(old, new)
        # Reflow only the seven edited entries; fields and examples keep their Markdown structure.
        for number in (185, 186, 210, 211, 248, 249, 251):
            pattern = rf'^### WAY-{number} .*?(?=^### WAY-|^## Withdrawn|\Z)'
            match = re.search(pattern, text, re.M | re.S)
            old = match.group()
            sections = old.split('\n\n')
            for index, section in enumerate(sections):
                if section and not section.startswith(('#', '-')):
                    sections[index] = textwrap.fill(section, width=98, break_long_words=False, break_on_hyphens=False)
            text = text.replace(old, '\n\n'.join(sections))
    else:
        text = text.replace('where no difference with a consequence remains, recommend the simplest and cheapest. Keep the\n  human\'s preferred tool as the proposal, and leave the choice to the human in this task',
                            'keep the human\'s preferred tool as the recommendation, and otherwise recommend the simplest\n  and cheapest where no difference with a consequence remains. Leave the choice to the human\n  in this task')
        if '/coding/' in relative:
            text = text.replace('Give each research question\n  to a fresh agent of its own,', 'Give each standing check\n  to a fresh agent of its own,')
        # Reflow only paragraphs/bullets containing newly overlong lines.
        paragraphs = text.split('\n\n')
        for index, paragraph in enumerate(paragraphs):
            if not any(len(line) > 100 for line in paragraph.splitlines()) or paragraph.startswith(('---', '|', 'name:', 'description:')):
                continue
            lines = paragraph.splitlines()
            groups = []
            for line in lines:
                if line.startswith('- ') or (line and not line.startswith(' ') and not groups):
                    groups.append([line])
                elif groups:
                    groups[-1].append(line)
            # These affected groups contain no nested bullets.
            if any(line.startswith('  - ') for line in lines):
                continue
            if groups:
                paragraphs[index] = '\n'.join(textwrap.fill(' '.join(group), width=98,
                    subsequent_indent='  ' if group[0].startswith('- ') else '',
                    break_long_words=False, break_on_hyphens=False) for group in groups)
        text = '\n\n'.join(paragraphs)
        text = text.replace('extension — step 2, and step 3 where\n  screens changed since the styleguide was written.',
                            'extension — step 2, and step 3 where screens changed since the styleguide was written.')
    path.write_bytes(text.replace('\n', newline).encode('utf-8'))
print('Refined recommendation precedence and line wrapping')
