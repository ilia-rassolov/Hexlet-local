def each2d(test, matrix):

    print(all(x for x in (all(test(elem) for elem in lst) for lst in matrix)))


def some2d(test, matrix):

    print(any(x for x in (any(test(elem) for elem in lst) for lst in matrix)))


def sum2d(test, matrix):

    print(sum((x for x in (sum(elem for elem in lst if test(elem)) for lst in matrix))))


def is_even(x):
    return x % 2 == 0


matrix = [[-1, 2, -3], [4, -5, 6]]

each2d(is_even, matrix)
print('**************')

some2d(is_even, matrix)
print('////////////////')

sum2d(is_even, matrix)
