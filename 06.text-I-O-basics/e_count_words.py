
from pathlib import Path
from collections import Counter


def count_words():
    data = open("file_path_1.txt").read()
    print(data)
    punctuation = [',', '.', '?', '!', ':']
    words = []
    for word in data.split():
        word = word.lower()
        for p in punctuation:
            if word.endswith(p):
                word = word[:-1]
        words.append(word)
    return Counter(words)


print(count_words())