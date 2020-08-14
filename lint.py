from glob import *
from pprint import *
import re
import os

lint_header = lambda str: str.split('>')[1].split('<')[0]

def remove_link(fname):
    with open(f'{fname}', encoding='utf-8') as f:
        content = f.read()
    HEADER_PATTERN = '^#+.*'
    with open(f'{fname}', 'w', encoding='utf-8') as f:
        lst = []
        lines = content.split('\n')
        for line in content.split('\n'):
            header = re.findall(HEADER_PATTERN, line)
            if header:
                header = header[0]
                if '<a name=' not in header:
                    continue
                if 'https://ccss17.github.io' in header:
                    continue
                level, value = header.split(' ', maxsplit=1)
                print(header)
                lst.append(f'{level} {lint_header(header)}')
            else:
                lst.append(line)
        f.write('\n'.join(lst))

def tag2note(fname):
    with open(f'{fname}', encoding='utf-8') as f:
        content = f.read()
    START = '<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">'
    END = '</blockquote>'
    content = content.split(START)
    with open(f'{fname}', 'w', encoding='utf-8') as f:
        for i, def_section in enumerate(content):
            def_section = def_section.split(END)
            if len(def_section) == 2:
                f.write('!!! tldr ""\n\n')
                for line in def_section[0].strip().split('\n'):
                    f.write(' ' * 4 + line + '\n')
                f.write('\n')
                f.write(def_section[1].strip() + '\n')
                f.write('\n')
            else:
                f.write(def_section[0]+'\n')

md_list = glob('docs/**/*.md', recursive=True)
for md in md_list:
    # if md.endswith('-test.md'):
    #     os.remove(md)
    tag2note(md)
    # remove_link(md)
