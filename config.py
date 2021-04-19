from bs4 import BeautifulSoup
import glob

def create_def_link():
    for path in glob.glob('site/**/*.html', recursive=True):
        with open(path, encoding='utf-8') as f:
            html = f.read()

        soup = BeautifulSoup(html, 'lxml')

        for i, defs in enumerate(soup.select('div.tldr')):
            defs['id'] = repr(i)
            defs.wrap(soup.new_tag('a', href='#' + repr(i)))

        with open(path, 'w', encoding='utf-8') as f:
            f.write(str(soup))

if __name__ == '__main__':
    create_def_link()