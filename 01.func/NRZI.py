from functools import reduce


def decode(graphic_string):

    result_list = [0]
    if graphic_string[0] == "|":
        result_list = [1]
    print(result_list)

    graphic_item_list = list(filter(lambda x: x != '|', graphic_string))
    print(graphic_item_list)

    def func(x, y):

        if y == x:
            result_list.append(0)
        else:
            result_list.append(1)
        print(result_list)
        return y


    result = list(reduce(func, graphic_item_list))
    print(result)


decode('¯¯¯|___|¯|_')


# NOT CORRECT CODE!











