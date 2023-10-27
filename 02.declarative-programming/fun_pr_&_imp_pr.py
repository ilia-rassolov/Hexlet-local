def remove_even(values):
    if len(values) < 2:
        return values

    del values[1::2]
    print(values)


def keep_odds_from_odds(collection):

    remove_even(collection)

    for nested_list in collection:
        print(nested_list)
        remove_even(nested_list)


l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
keep_odds_from_odds(l)
print(l)
print('-' * 20)

def remove_even_func(values):
    if len(values) < 2:
        return values
    return list(map(lambda x: x[1], filter(lambda x: x[0] % 2 == 0, enumerate(values))))


def odds_from_odds(collection):

    selection = remove_even_func(collection)


    print(list(map(remove_even_func, selection)))
 #   print(selection, '%')

l = [
            [1, 2, 3, 4, 5],
            ['c', 'a', 't'],
            ['d', 'o', 'g'],
            [100, 200, 300, 400],
            [True, False],
            [],
            [],
        ]
odds_from_odds(l)
# print(l, '//')