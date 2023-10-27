
from functools import wraps


def memoizing(max_memory):

    def wrapper(func):

        memory = {}
        list_arguments = []
        @wraps(func)

        def inner(arg):

            def add_value():

                result = func(arg)
                memory[arg] = result
                list_arguments.append(arg)
                print(list_arguments)
                print(memory)
                return result

            if arg in memory:
                print(memory.get(arg))
                return memory.get(arg)
            else:
                if len(memory) < max_memory:
                    add_value()
                else:
                    oldest_argument = list_arguments[0]
                    memory.pop(oldest_argument)
                    list_arguments.pop(0)
                    add_value()


        return inner
    return wrapper

@memoizing(3)
def f(x):
    print('Calculating...')
    print(x * 10)
    return x * 10

help(f)

f(1)
f(1)
f(2)
f(3)
f(4)
f(1)
f(2)



arguments = []
@memoizing(3)
def inc(argument):
    arguments.append(argument)
    return argument + 1

inc(inc(inc(0)))

