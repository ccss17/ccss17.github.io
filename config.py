from bs4 import BeautifulSoup
import glob
import hashlib
import yaml
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
                child_data[child].split('.')[0]+'>'+str(child)+'</a>'
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
    import os
    if os.path.isfile('docs/index.md'):
        os.remove('docs/index.md')
    tree.save2file('docs/index.md', key=lambda x: x.bpointer,
                   line_type='ascii-ex')

    with open('docs/index.md', encoding='utf-8') as f:
        index = f.read()
    index = index.replace(' ', '&nbsp;')
    index = index.replace('<a&nbsp;', '<a ')
    result = []
    for line in index.split('\n'):
        result.append(line+'</p><p>')
    with open('docs/index.md', 'w', encoding='utf-8') as f:
        f.write('<div class="index"><p>' + '\n'.join(result) + '</p></div>')


if __name__ == '__main__':
    create_def_link()
    create_category()
