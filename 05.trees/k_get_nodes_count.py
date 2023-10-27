from hexlet import fs

def get_nodes_count(node):
    if fs.is_file(node):
        return 1
    children = fs.get_children(node)
    descendant_counts = list(map(get_nodes_count, children))
    return 1 + sum(descendant_counts)

tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkfile('bashrc'),
        fs.mkfile('consul.cfg'),
    ]),
    fs.mkfile('hexletrc'),
    fs.mkdir('bin', [
        fs.mkfile('ls'),
        fs.mkfile('cat'),
    ]),
])

print(get_nodes_count(tree))

