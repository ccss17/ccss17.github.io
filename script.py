import re

DEF_PATTERN = '- .+ :'
THEOREM_PATTERN = '### \*\*<center>.+</center>\*\*'

def get_definitions(file):
    with open(file, encoding='utf-8') as f:
        content = f.read()
    definitions = re.findall(DEF_PATTERN, content)
    definitions = ', '.join((definition[2:-2] for definition in definitions))
    return definitions

def math_section(title, file):
    return f'''
- [{title}](https://ccss17.github.io/{file}.html)
    
  - {get_definitions('memos/'+file+'.md')}'''

def get_theorem():
    with open('memos/all.md', encoding='utf-8') as f:
        content = f.read()
    definitions = re.findall(THEOREM_PATTERN, content)
    definitions = '\n\n'.join(('- '+definition[14:-11] for definition in definitions))
    return definitions

def update():
    theorems = f'''\
## [생각 메모](https://ccss17.github.io/all.html)

{get_theorem()}

'''
    math_sections = f'''\
## 수학 메모
{math_section('논리학 ', 'logic')}
{math_section('수학 메모1', 'math')}
{math_section('수학 메모2', 'math2')}
{math_section('수학 메모3', 'math3')}
{math_section('수학 메모4', 'math4')}

### 미적분 메모
{math_section('극한 메모', 'calculus')}
{math_section('미분 메모', 'calculus2')}
{math_section('적분 메모', 'calculus3')}
{math_section('미분2 메모', 'calculus4')}
{math_section('적분2 메모', 'calculus5')}

### 선형대수학 메모
{math_section('1장 : 선형방정식', 'la')}
{math_section('2장 : 행렬 대수', 'la2')}
{math_section('3장 : 행렬식', 'la3')}

'''

    with open('memos/index.md', encoding='utf-8') as f:
        index = f.read()
    # all = index.find("## 생각 메모")
    # index = index[:all] + theorems
    # index += math_sections
    math = index.find("## 수학 메모")
    index = index[:math] + math_sections
    index += theorems
    with open('memos/index.md', 'w', encoding='utf-8') as f:
        f.write(index)
    with open('readme.md', 'w', encoding='utf-8') as f:
        f.write(index)
    print('생각 정리와 수학 정의 섹션들이 index.md 와 readme.md 에 업데이트됨')

def main():
    update()

if __name__ == '__main__':
    main()