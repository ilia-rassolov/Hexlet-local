# BEGIN (write your solution here)
def fill(coll, value, begin=0, end=None):
    if not end:
        end = len(coll)
    i = 0
    for x in coll:
        if i >= begin and i < end:
            coll[i] = value
        i += 1
    return coll

# END
print(fill([1, 2, 3, 4, 5, 6, 7, 8], '*', 3, 3))

print([1, 2, 3, 4, 5, 6, 7, 8][2:2])