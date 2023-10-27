from operator import add, sub


def partial_apply(inner, argument_1):

    def closure(argument_2):
        return inner(argument_1, argument_2)
    return closure


def flip(inner_2):

    def closure_2(arg_1, arg_2):
        return inner_2(arg_2, arg_1)
    return closure_2

argument_2 = [1, 2]
result = list(
        map(partial_apply(add, 10), argument_2),
    )
print(result)

arg_1 = 3
arg_2 = 4
result_2 = flip(sub)(3, 4)
print(result_2)

