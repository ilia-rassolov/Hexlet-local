def barchart(sequence):

    number_of_lines = abs(min(sequence)) + abs(max(sequence))

    def define_symbol(item_seq):

        if item_seq > 0:
            if max(sequence) - i > item_seq or i >= max(sequence):
                return ' '
            else:
                return '*'
        else:
            if i + 1 > abs(max(sequence)) + abs(item_seq) or i < max(sequence):
                return ' '
            else:
                return '#'

    result = ''
    for i in range(number_of_lines):
        list_simbol = list(map(define_symbol, sequence))
        string_simbol = ''.join(list_simbol)
        result += '\n' + string_simbol + '\n'
    result = result[:-1]
    print(result)
    return result


print(barchart([11, 10, -5, -3, -6]))

