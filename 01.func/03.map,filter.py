
def filter_map(func, iterable) -> list:

    result = []
    for item in iterable:
        if func(item)[0]:
            result.append(func(item)[1])
    print(result)
    return result


def make_stars(x):
    if x > 0:
        return True, '*' * x
    return False, ''


iterable = [1, 0, 5, -5, 2]

filter_map(make_stars, iterable)