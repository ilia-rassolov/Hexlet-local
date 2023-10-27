

def get_unique(*args):

    list_total = []
    for ls in args:
        list_total.extend(ls)
    print(list_total)
    set_current = set(list_total)
    print(set_current)
    list_result = list(set_current)
    print(list_result)


get_unique([1, 2, 3], [3, 4, 5], [5, 6, 7])
