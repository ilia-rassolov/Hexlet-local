# input_file = open("input.txt", "r")
# output_file = open("output.txt", "w")
# for i, line in enumerate(input_file, 1):
#     output_file.write(f"{i}) {line}")
# input_file.close()
# output_file.close()



a = open("in_1.txt", "w")
str1 = 'cat\ndog'
lst = str1.split('\n')
a.writelines(lst)
a.close()
py = open("in_1.txt")
for p in py:
    print(p)


# out1e = open("out_1.txt", "w")
# for i, line in enumerate(input_file, 1):
#     output_file.write(f"{i}) {line}")
# input_file.close()
# output_file.close()