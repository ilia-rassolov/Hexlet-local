from hexlet import fs
import copy

def to_upper(node):
    name = fs.get_name(node)
    new_meta = copy.deepcopy(fs.get_meta(node))
    if fs.is_file(node):
      return fs.mkfile(name.upper(), new_meta)
    return fs.mkdir(name.upper(), fs.get_children(node), new_meta)

def map_tree(func, tree):
    if not fs.get_children(tree):
        return func(tree)
    children = fs.get_children(tree)
    new_children = list(map(lambda child: map_tree(func, child), children))
    new_tree = func(tree)
    new_tree['children'] = new_children
    return new_tree



tree = fs.mkdir('/', [
  fs.mkdir('abc', [fs.mkdir('src',[
    fs.mkfile('solution1.py', meta={'size': 12},),
fs.mkfile('solution2.py', meta={'size': 32})
  ])]),
    fs.mkfile('solution20.py', meta={'size': 122}),
])

# {'name': '/',
#  'children': [{'name': 'SRC',
#    'children': [{'name': 'SOLUTION.PY', 'meta': {'size': 12}, 'type': 'file'}],
#    'meta': {},
#    'type': 'directory'}],
#  'meta': {},
#  'type': 'directory'}
def inner(file):
    name = fs.get_name(file)
    if fs.is_file(file):
        if '1' in name:
            return True
        return False
def filter_tree(bool_func, node):
    if fs.is_file(node):
        if bool_func(node):
            return node
        return []
    new_meta = copy.deepcopy(fs.get_meta(node))
    children = fs.get_children(node)
    print(children, '111', len(children))
    new_children = list(map(lambda child: filter_tree(bool_func, child), children))
    print(children, '222', len(children))
    print(new_children, '333', len(new_children))
    # print(new_children)
    return fs.mkdir(fs.get_name(node), new_children, new_meta)


print(filter_tree(inner, tree))

# {'name': '/',
#  'children': [{'name': 'src',
#    'children': [],
#    'meta': {},
#    'type': 'directory'}],
#  'meta': {},
#  'type': 'directory'}