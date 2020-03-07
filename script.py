import re
import glob 

DEF_PATTERN = '- .+ :'
MARKDOWN_PATH = 'memos/*.md'

def get_definitions(file):
    with open(file, encoding='utf-8') as f:
        content = f.read()
    definitions = re.findall(DEF_PATTERN, content)
    definitions = ', '.join((definition[2:-2] for definition in definitions))
    return definitions

def get_mdpath():
    return [f for f in glob.glob(MARKDOWN_PATH)]

def get_mathmdpath():
    mathmd = [
        'math.md',
        'math2.md',
        'math3.md',
        'math4.md',
        'la.md',
        'la2.md',
        'la3.md',
        'la4.md',
        'calculus.md',
        'calculus2.md'
    ]
    return ['memos/' + m for m in mathmd]

print('## 수학 메모')
print()
print('- [수학 메모1](https://ccss17.github.io/math.html)')
print()
print('  - ' + get_definitions('memos/math.md'))
print()
print('- [수학 메모2](https://ccss17.github.io/math2.html)')
print()
print('  - ' + get_definitions('memos/math2.md'))
print()
print('- [수학 메모3](https://ccss17.github.io/math3.html)')
print()
print('  - ' + get_definitions('memos/math3.md'))
print()
print('- [수학 메모4](https://ccss17.github.io/math4.html)')
print()
print('  - ' + get_definitions('memos/math4.md'))
print()
print('### 미적분 메모')
print()
print('- [극한 메모](https://ccss17.github.io/calculus.html)')
print()
print('  - ' + get_definitions('memos/calculus.md'))
print()
print('- [미적분 메모](https://ccss17.github.io/calculus2.html)')
print()
print('  - ' + get_definitions('memos/calculus2.md'))
print()
print('### 선형대수학 메모')
print()
print('- [1장 : 선형방정식](https://ccss17.github.io/la.html)')
print()
print('  - ' + get_definitions('memos/la.md'))
print()
print('- [2장 : 행렬 대수](https://ccss17.github.io/la2.html)')
print()
print('  - ' + get_definitions('memos/la2.md'))
print()
print('- [3장 : 행렬식](https://ccss17.github.io/la3.html)')
print()
print('  - ' + get_definitions('memos/la3.md'))
print()