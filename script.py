import re
import clipboard

DEF_PATTERN = '- .+ :'

def get_definitions(file):
    with open(file, encoding='utf-8') as f:
        content = f.read()
    definitions = re.findall(DEF_PATTERN, content)
    definitions = ', '.join((definition[2:-2] for definition in definitions))
    return definitions

def section(title, file):
    return f'''
- [{title}](https://ccss17.github.io/{file}.html)
    
  - {get_definitions('memos/'+file+'.md')}
    
    '''

str = f'''\
## 수학 메모
{section('수학 메모1', 'math')}
{section('수학 메모2', 'math2')}
{section('수학 메모3', 'math3')}
{section('수학 메모4', 'math4')}
### 미적분 메모
{section('극한 메모', 'calculus')}
{section('미분 메모', 'calculus2')}
{section('적분 메모', 'calculus3')}
### 선형대수학 메모
{section('1장 : 선형방정식', 'la')}
{section('2장 : 행렬 대수', 'la2')}
{section('3장 : 행렬식', 'la3')}
'''

clipboard.copy(str)
print('수학 정의 섹션이 클립보드에 복사됨')