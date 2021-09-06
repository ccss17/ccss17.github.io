import glob
import hashlib
import os

import yaml
from bs4 import BeautifulSoup
from treelib import Node, Tree


def hash(w):
    return hashlib.md5(w.encode('utf-8')).hexdigest()[:9]


def create_def_link(path):
    for path in glob.glob(path + '/**/*.html', recursive=True):
        with open(path, encoding='utf-8') as f:
            html = f.read()

        soup = BeautifulSoup(html, 'lxml')

        for defs in soup.select('div.def'):
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
                   child_data[child].rsplit('.', maxsplit=1)[0] +\
                   '>'+str(child)+'</a>'
            tree.create_node(node, node, parent=parent)
            continue
        tree.create_node(child, child, parent=parent)
        create_tree_from_dict(tree, child_data, child)


def create_category(yml_path, index_path, root_name):
    with open(yml_path, encoding='utf-8') as f:
        index = f.read()

    nav = yaml.load(index)['nav']
    del nav[0]
    nav = {root_name: nav}

    tree = Tree()
    root = next(iter(nav))
    tree.create_node(root, root)
    create_tree_from_dict(tree, nav, root)

    if os.path.isfile(index_path):
        os.remove(index_path)
    tree.save2file(index_path, key=lambda x: x.bpointer,
                   line_type='ascii-exr')

    with open(index_path, encoding='utf-8') as f:
        index = f.read()

    index = index.replace(' ', '&nbsp;') \
                 .replace('<a&nbsp;', '<a ') \
                 .replace('\n', '</p><p>\n') \
                 .replace('/README', '')
    print(index)

    index = '<div class="index"><p>' + index + '</p></div>'

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index)


if __name__ == '__main__':
    import sys
    if sys.argv[1] == '-d':
        create_def_link('site')
    elif sys.argv[1] == '-c':
        create_category('mkdocs.yml', 'docs/index.md', 'root')
    else:
        print('Invalid argument')
