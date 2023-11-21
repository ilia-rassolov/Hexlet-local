from hexlet import fs
import copy
from functools import reduce


def to_upper(node):
    name = fs.get_name(node)
    new_meta = copy.deepcopy(fs.get_meta(node))
    if fs.is_file(node):
      return fs.mkfile(name.upper(), new_meta)
    return fs.mkdir(name.upper(), fs.get_children(node), new_meta)


def map_tree(func, tree):
    if fs.is_file(tree):
        return func(tree)
    children = fs.get_children(tree)
    new_children = list(map(lambda child: map_tree(func, child), children))
    new_meta = copy.deepcopy(fs.get_meta(tree))
    new_tree = func(tree)
    return fs.mkdir(fs.get_name(new_tree), new_children, new_meta)


tree_ = fs.mkdir('/', [
fs.mkdir('empty', []),
fs.mkdir('first_1', [fs.mkdir('first_inner_12', [
    fs.mkfile('solution1.py', meta={'size': 12},),
    fs.mkfile('solution11.py', meta={'size': 32})
  ])]),
fs.mkfile('solution100.py', meta={'size': 122}),
fs.mkdir('first_2', [
    fs.mkfile('solution2.py', meta={'size': 12},),
    fs.mkfile('solution22.py', meta={'size': 32})
  ]),
])

# print(map_tree(to_upper, tree))

# {'name': '/',
#  'children': [{'name': 'SRC',
#    'children': [{'name': 'SOLUTION.PY', 'meta': {'size': 12}, 'type': 'file'}],
#    'meta': {},
#    'type': 'directory'}],
#  'meta': {},
#  'type': 'directory'}


def inner(node):
    name = fs.get_name(node)
    return '2' in name


def filter_tree(bool_func, node):
    children = fs.get_children(node)
    new_meta = copy.deepcopy(fs.get_meta(node))
    filter_children = list(filter(lambda child: bool_func(child), children))
    new_children = list(map(lambda new_child: filter_tree(bool_func, new_child), filter_children))
    return fs.mkdir(fs.get_name(node), new_children, new_meta)


# print(filter_tree(inner, tree))
# def reduce(func, iterable, initial):
#     acc = initial
#     for item in iterable:
#         acc = func()
# Подсчитываем количество узлов в дереве:
# f = lambda acc, _: acc + 1
# a = [4, 3, 6, 9]
# x = f(0, a)
# print(x, ' = x')
# print(reduce(f, a, 0), ' = reduce')
def reduce_tree(func, tree, acc):
    print('tree =', tree)
    if fs.is_file(tree):
        print('res_file = ', func(tree, acc))
        return func(tree, acc)
    children = fs.get_children(tree)
    print('children = ', children)

    if not children:
        res = func(tree, acc)
        print('res empt-dir = ', res)
        return res
    result = acc
    for child in children:
        res = reduce_tree(func, child, result)
        if fs.is_directory(child):
            if fs.get_children(child):
                result = func(child, res)
        result = res
        print('result = ', result)
    return result


    # result = reduce(lambda _, child: reduce_tree(func, child, acc), children, acc)
    # return result

# print(reduce_tree(inner, tree))



print(reduce_tree(lambda _, acc: acc + 1, tree_, 0))
