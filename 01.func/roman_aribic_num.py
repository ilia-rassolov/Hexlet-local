

def to_roman(num_arabic):

    list_num_arabic = [int(a) for a in str(num_arabic)]
    list_num_arabic.reverse()
    iter_num = list(enumerate(list_num_arabic))
    print(list_num_arabic)
    print(iter_num)


    def to_roman_dijit(x):

        num_roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        n = x[0] # разряд арабского числа
        if x[1] in range(4):
            result = num_roman[n * 2] * x[1]
        elif x[1] in range(4, 6):
            result = num_roman[n * 2] * (5 - x[1]) + num_roman[1 + n * 2]
        elif x[1] in range(6, 8):
            result = num_roman[1 + n * 2] + num_roman[n * 2] * (x[1] - 5)
        else:
            result = num_roman[n * 2] * (10 - x[1]) + num_roman[2 + n * 2]
        return result

    string_roman = list(map(to_roman_dijit, iter_num))
    string_roman.reverse()
    result = ''.join(string_roman)
    print(result)
    return result


def to_arabic(num_roman):

    def calcle(''): NOT_CORRECT !!!





to_roman('3409')


