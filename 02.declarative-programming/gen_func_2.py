
def intersperse(source, delimiter):

    result = [source[0]]
    cursor = iter(source[1:])
    for x in source[1:]:
        result.append(delimiter)
        result.append(x)
        i = iter(result)
        yield i

def result_iter():
    for n in intersperse(range(4), 0):
        print(intersperse(range(4), 0), '****')

i = intersperse(range(4), 0)



print(type(intersperse))
print(intersperse(range(4), 0), '?????????')
print(list(intersperse(range(4), 0)), '///')
result_iter()



# NOT CORRECT CODE!


