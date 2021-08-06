import glob
import hashlib
import os

import yaml
from bs4 import BeautifulSoup
from treelib import Node, Tree


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


def create_tree_from_dict(tree, data, parent=None):
    root = next(iter(data))
    for child_data in data[root]:
        child = next(iter(child_data))
        if isinstance(child_data[child], str):
            node = '<a href=' + \
                   child_data[child].rsplit('.', maxsplit=1)[0]+\
                   '>'+str(child)+'</a>'
            tree.create_node(node, node, parent=parent)
            continue
        tree.create_node(child, child, parent=parent)
        create_tree_from_dict(tree, child_data, child)


def create_category():
    with open('mkdocs.yml', encoding='utf-8') as f:
        index = f.read()

    nav = yaml.load(index)['nav']
    del nav[0]
    nav = {'ccss17': nav}

    tree = Tree()
    root = next(iter(nav))
    tree.create_node(root, root)
    create_tree_from_dict(tree, nav, root)

    index_path = 'docs/index.md'
    if os.path.isfile(index_path):
        os.remove(index_path)
    tree.save2file(index_path, key=lambda x: x.bpointer,
                   line_type='ascii-exr')

    with open(index_path, encoding='utf-8') as f:
        index = f.read()

    index = index.replace(' ', '&nbsp;') \
                 .replace('<a&nbsp;', '<a ') \
                 .replace('\n', '</p><p>\n') \
                 .replace('ccss17', '<i class="fas fa-fire"></i>')
    index = '<div class="index"><p>' + index + '</p></div>'

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index)


if __name__ == '__main__':
    create_def_link()
    create_category()
