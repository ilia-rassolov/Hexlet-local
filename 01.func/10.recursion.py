
def length(list_: list):

    if not list_:
        return 0
    list_.pop(0)
    return 1 + length(list_)


def reverse_range(begin, end) -> list:

    if begin == end:
        return [end]

    return [end] + reverse_range(begin, end - 1)

def filter_positive(start_list):

    if len(start_list) == 0:
        return []
    head = start_list[0]
    tail = start_list[1:]
    if head <= 0:
        return filter_positive(tail)
    return [head] + filter_positive(tail)




