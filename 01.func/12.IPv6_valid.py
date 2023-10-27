from string import hexdigits
from collections import Counter


def is_valid_ipv6(ip_v6):

    if ip_v6 == '::':
        return True

    set_true = set()

    list_ip_v6 = ip_v6.split(':')
    print(list_ip_v6)

    if len(list_ip_v6) > 2:
        if list_ip_v6[0] == list_ip_v6[1] == '':
            list_ip_v6.pop(0)
        if list_ip_v6[-1] == list_ip_v6[-2] == '':
            list_ip_v6.pop()
    print(list_ip_v6)

    count = Counter(list_ip_v6)
    print(count)
    set_true.add(count[''] < 2)
    print(set_true)

    if '' not in list_ip_v6:
        set_true.add(len(list_ip_v6) == 8)
    print(set_true)

    set_true.add(len(list_ip_v6) < 9)
    print(set_true)

    def check_char_group(char_group):
        set_true.add(len(char_group) < 5)
        set_true.add(set(char_group) | set(hexdigits) == set(hexdigits))
        return set_true
    result = list(map(check_char_group, list_ip_v6))
    print(set_true, 'total')
    print(set_true == {True})
    return set_true == {True}


is_valid_ipv6(':1')