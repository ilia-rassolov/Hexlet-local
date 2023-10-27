from collections import Counter
from functools import reduce


def filter_anagrams(word, iterable):

    def check_anagram(string):

        counter_1 = Counter(word)
        counter_2 = Counter(string)
        if counter_1 == counter_2:
            return string

    return filter(check_anagram, iterable)



result = list(filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(result)
print(tuple(filter_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])))
print(list(filter_anagrams([1, 2], [[2, 1], [2, 2], [1, 2]])))
print(list(filter_anagrams((1, 2), ((2, 1), (2, 2), (1, 2)))))
empty = ''
print(list(filter_anagrams(empty, [empty, 'foo', empty])))
print('/////')

def same_parity_filter(start_list):

    if len(start_list) == 0:
        return []
    n = start_list[0] % 2
    return list(filter(lambda x: x % 2 == n, start_list))

result = same_parity_filter([2, 0, 1, -3, 10, -2])
print(result)
print(same_parity_filter([1, 2, 0, 1, -3, 10, -2]))
print('***')


def find_index_of_nearest(desired_number, list_):

    if len(list_) == 0:
        return None

    enumerate_list = list(enumerate(list_))

    def compare(tuple_1, tuple_2):
        if abs(tuple_1[1] - desired_number) <= abs(tuple_2[1] - desired_number):
            return tuple_1
        return tuple_2

    return reduce(compare, enumerate_list, enumerate_list[0])[0]


print(find_index_of_nearest(7, [15, 10, 3, 7, 7, 4]))
print('++++++++')
















