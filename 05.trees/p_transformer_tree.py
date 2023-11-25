# NOT CORRECT CODE !!!

import copy
def build_dict(tree_d):     # представление дерева словарём связей - {узел: (предок, [потомки])...}
    dictionary = {}

    def inner(tree_d, parent=None):
        if len(tree_d) == 1:
            dictionary[tree_d[0]] = (parent, [])
        else:
            [node, branches] = tree_d
            children = [branch[0] for branch in branches]
            dictionary[node] = (parent, children)
            for branch in branches:
                inner(branch, node)
    inner(tree_d)
    return dictionary

def build_path(node, tree_):     # создать путь узел - корень
    dictionary = build_dict(tree)
    path = [node]
    parent = dictionary[node][0]
    while parent:
        path.append(parent)
        parent = dictionary[path[-1]][0]
    return path


def transform(tree, node):
    dictionary = build_dict(tree)
    print(dictionary)
    path_new_root = build_path(node, tree)
    print(path_new_root)
    # new_dict_path_new_root = dict(map(lambda node_: node_: ()))
    for node_ in path_new_root:
        print('node_ = ', node_)
        (parent, children) = dictionary[node_]
        print('parent = ', parent, 'children = ', children)
        if children[0]:
            new_parent = copy.deepcopy(children[0])
        else:
            new_parent = None
        if parent:
            new_children = [parent] + children[1:]
        else:
            new_children = children[1:]
        dictionary[node_] = (new_parent, new_children)
        print(dictionary[node_])
        print(dictionary)
    #
    # return dictionary






tree = ['A', [       #     A
    ['B', [          #    / \
        ['D'],       #   B   C
    ]],              #  /   / \
    ['C', [          # D   E   F
        ['E'],
        ['F'],
    ]],
]]

# transform(tree, 'B')

# ['B', [                 #   B
#     ['D'],              #  / \
#     ['A', [             # D   A
#         ['C', [         #      \
#             ['E'],      #       C
#             ['F'],      #      / \
#         ]],             #     E   F
#     ]],
# ]]


transform(tree, 'B')
