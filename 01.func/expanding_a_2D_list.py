from operator import add, mul
from functools import reduce



curry = lambda f: lambda x: lambda y: f(x, y)  # noqa: E731
compose = lambda f: lambda g: lambda x: f(g(x))  # noqa: E731

pair = lambda x: [x, x]  # noqa: E731
dup = lambda x: x + x  # noqa: E731

def enlarge(image):


    double_string = list(map(curry(reduce)(dup)), image)

    print(double_string)

    double_large = []
    print(double_large)




print(enlarge([
    '****',
    '*  *',
    '*  *',
    '****'
]))

# NOT CORRECT CODE!
