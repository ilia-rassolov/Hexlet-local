from collections import Counter


def calculate_probabilities(history):

    enumerate_history = list(enumerate(history))
    print(enumerate_history)

    num_next_num_total = {
        num: [next_num for (i, next_num) in enumerate_history[1:] if enumerate_history[i - 1][1] == num]
        for num in history[:]}
    print(num_next_num_total)

    result = {
        num: {
            next_num: Counter(next_numbers)[next_num] / len(next_numbers)
            for next_num in next_numbers}
            for num, next_numbers in num_next_num_total.items()}
    print(result)


calculate_probabilities([1, 2, 1, 5, 1, 3, 1, 6, 1, 2, 8])
# print(calculate_probabilities_for_numbers([1, 3, 1, 5, 1, 2, 1, 6, 5]))
