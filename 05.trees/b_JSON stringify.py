
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




def stringify(data, replacer=' ', spaces_count=1):
    if not isinstance(data, dict):
        return str(replacer)*int(spaces_count) + str(value)
    else:
        result = '{\n'
        for key in data:
            result += f'    {key}: {data1_str[key]}\n'


                if key in data2_str:
                    if data1_str[key] == data2_str[key]:

                    else:
                        result += (f'  - {key}: {data1_str[key]}\n  + '
                                   f'{key}: {data2_str[key]}\n')
                else:
                    result += f'  - {key}: {data1_str[key]}\n'
            else:
                result += f'  + {key}: {data2_str[key]}\n'
        result += '}'
