def flatten(start_list):
    result = []
    def inner(_lst):
        for item in _lst:
            if isinstance(item, list):
                inner(item)
            else:
                result.append(item)
    inner(start_list)
    return result

# def normalize(item):
#     return flatten(item) if isinstance(item, list) else [item]
#
#
# def flatten(tree):
#     return sum(map(normalize, tree), [])

print(flatten([2, [3, 5], [[4, 3], 2]]))