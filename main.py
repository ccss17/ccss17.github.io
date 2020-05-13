import re
import os

START_SECTION = '# <a name="수학 메모" href="#수학 메모">수학 메모</a>'

def get_definitions(file):
    DEF_PATTERN = '">\n\n.+ :'
    with open(file, encoding='utf-8') as f:
        content = f.read()
    definitions = re.findall(DEF_PATTERN, content)
    definitions = ', '.join((definition[4:-2] for definition in definitions))
    return definitions

def get_theorem(file):
    THEOREM_PATTERN = '### \*\*<center>.+</center>\*\*'
    with open(file, encoding='utf-8') as f:
        content = f.read()
    definitions = re.findall(THEOREM_PATTERN, content)
    definitions = '\n\n'.join(('  - ##### '+definition[14:-11] for definition in definitions))
    return definitions

def sections(title, file, get):
    return f'''
- {title}
    
  ###### [{get('memos/'+file+'.md')}](https://ccss17.github.io/{file}.html)'''

def update():
    theorems = f'''\
### 생각 메모

##### - [기초](https://ccss17.github.io/all.html)

##### - [생각](https://ccss17.github.io/all2.html)

##### - [수학 역사](https://ccss17.github.io/all3.html)

##### - [수학 역사2(수학의 확실성)](https://ccss17.github.io/all4.html)

##### - [컴퓨터 역사](https://ccss17.github.io/all5.html)

'''
# {sections('기초적인 것에 관련된 메모', 'all', get_theorem)}
# {sections('생각에 관련된 메모', 'all2', get_theorem)}
# {sections('역사에 관련된 메모', 'all3', get_theorem)}
    math_sections = f'''\
{START_SECTION}

### 수학기초론 메모

<blockquote style="border: 2px solid; color:black; background:#E0E0E0; padding: 7px;">

{sections('논리학', 'logic', get_definitions)}
{sections('집합론', 'math', get_definitions)}
{sections('수리논리학', 'mathmatical_logic', get_definitions)}

</blockquote>

### 산술과 대수학 메모

<blockquote style="border: 2px solid; color:black; background:#E0E0E0; padding: 7px;">
{sections('기초 산술 메모', 'arithmetic', get_definitions)}
{sections('추상대수학 메모', 'abstract_algebra', get_definitions)}
{sections('대수학 메모', 'algebra', get_definitions)}

</blockquote>

### 해석학 메모

<blockquote style="border: 2px solid; color:black; background:#E0E0E0; padding: 7px;">
{sections('해석학 메모', 'anal', get_definitions)}
{sections('삼각 함수 메모', 'trig', get_definitions)}
{sections('함수 메모', 'function', get_definitions)}

</blockquote>

### 확률 메모

<blockquote style="border: 2px solid; color:black; background:#E0E0E0; padding: 7px;">
{sections('조합 메모', 'comb', get_definitions)}
{sections('확률 메모', 'prop', get_definitions)}

</blockquote>

## 통계학 메모

<blockquote style="border: 2px solid; color:black; background:#E0E0E0; padding: 7px;">
{sections('도수분포의 평균,분산,표준편차', 'stat', get_definitions)}
{sections('이산확률변수의 평균,분산,표준편차', 'stat2', get_definitions)}
{sections('이항분포의 평균,분산,표준편차', 'stat3', get_definitions)}
{sections('연속확률변수의 평균,분산,표준편차와 정규분포', 'stat4', get_definitions)}
{sections('통계적 추정', 'stat5', get_definitions)}
{sections('상관관계 분석', 'stat6', get_definitions)}

</blockquote>

## 미적분 메모

<blockquote style="border: 2px solid; color:black; background:#E0E0E0; padding: 7px;">
{sections('극한 메모', 'calculus', get_definitions)}
{sections('미분 메모', 'calculus2', get_definitions)}
{sections('적분 메모', 'calculus3', get_definitions)}
{sections('미분2 메모', 'calculus4', get_definitions)}
{sections('적분2 메모', 'calculus5', get_definitions)}
{sections('벡터해석학 메모', 'vector', get_definitions)}
{sections('미적분 메모', 'calculus6', get_definitions)}

</blockquote>

## 선형대수학 메모

<blockquote style="border: 2px solid; color:black; background:#E0E0E0; padding: 7px;">
{sections('선형방정식', 'la', get_definitions)}
{sections('행렬 대수', 'la2', get_definitions)}
{sections('행렬식', 'la3', get_definitions)}
{sections('벡터공간', 'la4', get_definitions)}
{sections('고유벡터', 'la5', get_definitions)}
{sections('직교', 'la6', get_definitions)}

</blockquote>

'''

    with open('memos/index.md', encoding='utf-8') as f:
        index = f.read()
    math = index.find(START_SECTION)
    index = index[:math] + math_sections
    index += theorems
    with open('memos/index.md', 'w', encoding='utf-8') as f:
        f.write(index)
    with open('readme.md', 'w', encoding='utf-8') as f:
        f.write(index)

def subsection(fname, title, dic):
    with open(f'memos/{fname}.md', encoding='utf-8') as f:
        content = f.read()
    
    str=f'''\
# [ccss17.github.io](https://ccss17.github.io)

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

- ## **{title}**

'''
    for k, v in dic.items():
        str += f'  **[{k}](https://ccss17.github.io/{v}.html)**\n\n'
    str += '</blockquote>\n\n---'
    with open(f'memos/{fname}.md', 'w', encoding='utf-8') as f:
        f.write(str + content.split('---', maxsplit=1)[1])

def update_subsection(section, data):
    for title in data.values():
        subsection(title, section, data)

def link(fname):
    with open(f'memos/{fname}', encoding='utf-8') as f:
        content = f.read()
    HEADER_PATTERN = '^#+.*'
    with open(f'memos/{fname}', 'w', encoding='utf-8') as f:
        lst = []
        for line in content.split('\n'):
            header = re.findall(HEADER_PATTERN, line)
            if header:
                header = header[0]
                if 'https://ccss17.github.io' not in header\
                    and '<a name="' not in header:
                    level, value = header.split(' ', maxsplit=1)
                    lst.append(f'{level} <a name="{value}" href="#{value}">{value}</a>')
                else:
                    lst.append(line)
            else:
                lst.append(line)
        f.write('\n'.join(lst))

def linkable():
    for fname in os.listdir('memos'):
        link(fname)
    
if __name__ == '__main__':
    dic = {
        '기초' : 'all',
        '생각' : 'all2',
        '수학 역사(고대 그리스~19세기)' : 'all3',
        '수학 역사2(수학의 확실성)' : 'all4',
        '컴퓨터 역사' : 'all5'
    }
    update_subsection('생각 메모', dic)
    update()
    linkable()
    print('업데이트됨')
