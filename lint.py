from glob import *
from pprint import *
import re

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

md_list = glob('docs/**/*.md', recursive=True)
for md in md_list:
    print(md)
    remove_link(md)
