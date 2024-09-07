import glob
import os

def grep(substring, pattern):
    new_pattern = os.path.expanduser(pattern)
    print(new_pattern)
    paths = glob.glob(new_pattern)
    print('paths = ', paths)
    lines = []
    for path in paths:
        print('path = ', path)
        if not os.path.isdir(path):
            data = open(path)
            for line in data:
                if substring in line:
                    lines.append(line)
    return lines



print(grep('каталог', '~/PycharmProjects/HexletEx/m-2/06.text-I-O-basics/a_Global_search/*4.txt'))
