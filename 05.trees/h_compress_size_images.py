import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


def compress_images(tree):

    def change_size(node):
        name = get_name(node)
        if is_file(node) and name[-4:] == '.jpg':
            new_size = get_meta(node)['size'] / 2
            new_meta = copy.deepcopy(get_meta(node))
            new_meta['size'] = new_size
            return mkfile(get_name(node), new_meta)
        return node

    children = get_children(tree)
    new_children = list(map(change_size, children))
    new_meta = copy.deepcopy(get_meta(tree))
    tree2 = mkdir(get_name(tree), new_children, new_meta)
    return tree2


tree = mkdir(
    'my documents',
    [
        mkfile('avatar.jpg', {'size': 100}),
        mkfile('photo.jpg', {'size': 150}),
        mkfile('not_photo.aa',),
    ],
    {'hide': False}
)

print(compress_images(tree))

