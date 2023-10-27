

def updated(d: dict, **kwargs):

    copy_of_d = d.copy()
    print(copy_of_d)
    print(kwargs)

    if not kwargs:
        print(copy_of_d)
        return copy_of_d
    copy_of_d.update(kwargs)
    print(copy_of_d)

updated({'a': 1, 'b': None, 2: 4}, a=2)
