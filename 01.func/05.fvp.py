
from functools import reduce
from operator import truth, getitem



def keep_truthful(iterable):

    result = filter(truth, iterable)
    print(list(result))
    return result


def abs_sum(iterable):

    module_num = list(map(abs, iterable))
    print(module_num)

    result = sum(module_num, 0)
    print(result)
    return result


def walk(deep_nested_dictionary, path):

    result = reduce(getitem, path, deep_nested_dictionary)
    print(result)
    return result


keep_truthful([True, '', 1, 'asd'])

walk({'a': {7: {'b': 42}}}, ["a", 7, "b"])

abs_sum([-3, 7])







