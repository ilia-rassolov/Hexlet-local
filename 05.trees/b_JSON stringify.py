import copy
from functools import reduce
from itertools import repeat

def stringify (value, replacer=' ', spaces_count=1):
    if not isinstance(value, dict):
        return ''.join(repeat(replacer, spaces_count)) + str(value)

    def walk(data):
        if not isinstance(data, dict):
            return ''.join(repeat(replacer, spaces_count)) + str(value)
        def sum_string(string1, string2):
            return string1 + string2
    def return_key_value(k, v):
        if not isinstance(v, dict):
            return f"{stringify(k, replacer, spaces_count)}: {v}"

    items = list(data1.items())
    print(items)
    output = reduce(return_key_value, items)
    return output



# return walk(value)




    # for
    #
    # print(list_items)
    # def return_key_value(k, v):
    #     if not isinstance(v, dict):
    #         return f"{stringify(k)}: {v}"
    #     double_spaces_count = copy.deepcopy(spaces_count) * 2
    #
    #     return f"{stringify(k)}:\n{stringify(v, double_spaces_count)}"
    # return return_key_value("nested", {"count": 5})
# def return_dict(data):
#     items = list(iter(data.keys(), data.items()))
#
#     print(items)
#     result_current = map(return_key_value, items)
#     print(list(result_current))
#     return f"{stringify('{')}\n{stringify('{')}"

    # def inner(item):
    #     return stringify(item) if isinstance(item, list) else [item]
    #
    # result = '123'
    # return stringify('{')\nХочу\nПить!
    # items_list = list(value.items())
    # map(lambda k,v: )



# print(stringify ('string', replacer='-', spaces_count=3))
# print(stringify ('[string111, ert]'))
print(stringify(5, '*', 2))
# print(stringify(True))
# print(stringify(5, '_', 12))
data1 = {"hello": "world", "is": True, "2": "false", "nested": {"count": 5}}
print(stringify(data1, '_', 3))
# print(return_key_value('hello', 'world'))
# print(return_dict(data))
# print(return_key_value("hello", "world"))