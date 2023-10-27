

def memoized(func):
    memory = {}

    def inner(arg):

        if arg not in memory:
            result = func(arg)
            memory[arg] = result
            return result
        else:
            return memory.get(arg)

    return inner


