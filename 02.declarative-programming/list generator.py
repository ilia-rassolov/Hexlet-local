def non_empty_truths(list_of_lists):

    return [lst for lst in [[x for x in lst if x] for lst in list_of_lists] if lst]


print(non_empty_truths([[0, ""], [False, None], []]))
print(non_empty_truths([[False], [1], [], [2]]))