from bs4 import BeautifulSoup
import glob
import hashlib

def hash(w):
    return hashlib.md5(w.encode('utf-8')).hexdigest()[:9]

def create_def_link():
    for path in glob.glob('site/**/*.html', recursive=True):
        with open(path, encoding='utf-8') as f:
            html = f.read()

        soup = BeautifulSoup(html, 'lxml')

        for defs in soup.select('div.tldr'):
            hashed = hash(defs.text)
            defs['id'] = hashed
            defs.wrap(soup.new_tag('a', href='#' + hashed))

        with open(path, 'w', encoding='utf-8') as f:
            f.write(str(soup))

if __name__ == '__main__':
    create_def_link()