import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


def downcase_file_names(node):
    name = get_name(node)
    meta = get_meta(node)
    new_name = copy.deepcopy(name)
    new_name = new_name.lower()
    print(name, new_name)
    if is_file(node):
        return mkfile(new_name, meta)
    children = get_children(node)
    new_children = list(map(lambda child: downcase_file_names(child), children))
    new_tree = mkdir(name, new_children, meta)
    return new_tree

print(downcase_file_names({'name': 'Avatar.jpg', 'meta': {}, 'type': 'file'}))
print(downcase_file_names(
    {'name': 'my documents', 'children': [{'name': 'Avatar', 'meta': {'size': 50.0}, 'type': 'file'},
                                          {'name': 'pHOoto.jpg', 'meta': {'size': 75.0}, 'type': 'file'},
                                          {'name': 'not_phOTo.aa', 'meta': {}, 'type': 'file'}],
     'meta': {'hide': False}, 'type': 'directory'}))
