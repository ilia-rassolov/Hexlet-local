# product()  # хотя бы одна последовательность должна быть дана
# Traceback (most recent call last):
#    ...
# TypeError: product() missing 1 required positional argument: 'sequence'
# product([])
# []
def product(*args):
    if not args:
        raise TypeError("product() missing 1 required positional argument: 'sequence'")
    pools = [tuple(pool) for pool in args]
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    total = []
    for prod in result:
        total.append(tuple(prod))
    return total

# a = product()

# [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')]
# print(a)
print(product('hello', 'world'))
# []
# ^ если хотя бы одна из входных последовательностей пустая,
# то выходной список тоже будет пуст
