import itertools

def remove_first_level(tree):
    return list((itertools.chain. from_iterable(itertools.filterfalse(lambda x: type(x) != list, tree))))



print(remove_first_level([1, 2, [3, 5], [[4, 3], 2]]))