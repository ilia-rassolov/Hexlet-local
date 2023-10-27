def my_map(f, xs):

    for x in xs:
        yield f(x)


print(list(my_map(abs, [-1, 2, -3])))
print(type(my_map))
print('*' * 20)


def my_filter(f, xs):

    for x in xs:
        if f(x):
            yield x

def replicate_each(n, xs):

    for x in xs:
        for i in range(n):
            yield x


print(list(my_filter(lambda x: x % 2 == 1, range(10))))
print('/' * 20)


print(list(replicate_each(3, [1, 'a'])))
print(type(replicate_each))

