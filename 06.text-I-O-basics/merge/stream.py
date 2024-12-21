input_file = open("file_1.txt", "r")
output_file = open("out_file.txt", "w")
for i, line in enumerate(input_file, 1):
    output_file.write(f"{i}) {line}")
input_file.close()
output_file.close()