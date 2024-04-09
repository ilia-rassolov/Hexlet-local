def stringify(data, replacer=' ', spaces_count=1):
    INDENT = replacer * spaces_count

    def inner(data_, level=0):
        if not isinstance(data_, dict):
            return f"{INDENT*level}{data_}"
        level += 1
        result = '{\n'
        for key in data_:
            if not isinstance(data_[key], dict):
                result += f"{INDENT*level}{key}: {data_[key]}\n"
            else:
                result += f"{INDENT*level}{key}: {inner(data_[key], level)}\n"
        result += INDENT*(level - 1)
        result += '}'
        return result

    return inner(data)

import itertools


# # BEGIN
# def stringify(value, replacer=' ', spaces_count=1):
#
#     def iter_(current_value, depth):
#         if not isinstance(current_value, dict):
#             return str(current_value)
#
#         deep_indent_size = depth + spaces_count
#         deep_indent = replacer * deep_indent_size
#         current_indent = replacer * depth
#         lines = []
#         for key, val in current_value.items():
#             lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
#         result = itertools.chain("{", lines, [current_indent + "}"])
#         return '\n'.join(result)
#
#     return iter_(value, 0)
# # END