
from collections import Counter


def length_frequencies(iterable):

    return Counter(len(x) for x in iterable)




print(length_frequencies('Use the Force, Luke!'.split()))

