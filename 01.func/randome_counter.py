from collections import Counter
from random import randint


def roll_die():
    x = randint(1, 6)
    print(x)
    return x

def histo(rounds_count, roll_die):

    round_results = []
    for i in range(rounds_count):
        round_results.append(roll_die())
    print(round_results)
    game_result = Counter(round_results)
    print(game_result)


    for i in range(1, 7):
        if i in game_result.keys():
            print(f"{i}|{'#' * game_result[i]} {game_result[i]}")
        else:
            print(f"{i}|")


histo(10, roll_die)
