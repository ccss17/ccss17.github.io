import re

START = '- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;">\n\n'
END = '  </blockquote>\n\n'

def make_def_boxed(file):
    DEF_PATTERN = '- .+ :'
    fname = 'memos/'+file+'.md'
    with open(fname, encoding='utf-8') as f:
        content = f.read()
    
    wfname = 'memos/'+file+'.md'
    # wfname = 'memos/'+file+'_test.md'
    mode = False
    with open(wfname, 'w', encoding='utf-8') as f:
        for i, line in enumerate(content.split('\n')):
            if not line or line.isspace(): continue
            if not mode:
                if line[0] == '-':
                    f.write(START)
                    mode = True
            else:
                if line[0] == '-':
                    f.write(END)
                    f.write(START)
                elif line[2] == '-' or line[0] == '#':
                    f.write(END)
                    mode = False
            f.write(line+'\n\n')

if __name__ == '__main__':
    # make_def_boxed('logic')
    # make_def_boxed('math')
    # make_def_boxed('mathmatical_logic')
    # make_def_boxed('arithmetic')
    # make_def_boxed('abstract_algebra')
    # make_def_boxed('algebra')
    # make_def_boxed('anal')
    # make_def_boxed('trig')
    # make_def_boxed('function')
    # make_def_boxed('prop')
    # make_def_boxed('stat')
    # make_def_boxed('calculus')
    # make_def_boxed('calculus2')
    # make_def_boxed('calculus3')
    # make_def_boxed('calculus4')
    # make_def_boxed('calculus5')
    # make_def_boxed('vector')
    # make_def_boxed('calculus6')
    # make_def_boxed('la')
    # make_def_boxed('la2')
    # make_def_boxed('la3')
    # make_def_boxed('la4')
    # make_def_boxed('la5')
    # make_def_boxed('la6')