import copy
from hexlet import fs

def change_owner_tree(tree):
    def change_owner(node, owner):
        name = fs.get_name(node)
        new_meta = copy.deepcopy(fs.get_meta(node))
        new_meta['owner'] = owner
        if fs.is_file(node):
            return fs.mkfile(name, new_meta)

        children = fs.get_children(node)
        new_children = list(map(lambda child: change_owner(child, owner), children))
        new_tree = fs.mkdir(name, new_children, new_meta)
        return new_tree



