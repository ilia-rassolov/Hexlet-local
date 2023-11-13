def merge(file1, file2, out):
    with open(file1) as input_1:
        with open(file2) as input_2:
            with open(out, "w") as output_file:
                for line1, line2 in zip(input_1, input_2):
                    if line1 == line2:
                        output_file.write(line1)
                    else:
                        output_file.write(f"'>>>file1>>>', '\n', {line1}, '\n', '=====', '\n'. {line2}, '>>>file2>>>', '\n'")


merge('file_1.txt', 'file_2.txt', 'out_file.txt')


