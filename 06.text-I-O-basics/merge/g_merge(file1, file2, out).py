def merge(file1, file2, out):
    with open(file1) as input_1:
        with open(file2) as input_2:
            with open(out, "w") as output_file:
                def write_stack(s1, s2):
                    if s1 or s2:
                        output_file.write('>>>file1>>>\n')
                        output_file.writelines(s1)
                        output_file.write('=====\n')
                        output_file.writelines(s2)
                        output_file.write('<<<file2<<<\n')
                stack1 = []
                stack2 = []
                for line1, line2 in zip(input_1, input_2):
                    if line1 == line2:
                        print(stack1, ' - stack1 in cicle')
                        print(stack2, ' - stack2 in cicle')
                        write_stack(stack1, stack2)
                        output_file.write(line1)
                        stack1 = []
                        stack2 = []
                    else:
                        stack1.append(line1)
                        stack2.append(line2)
                print(stack1, ' - stack1')
                print(stack2, ' - stack2')
                write_stack(stack1, stack2)


merge('file_1.txt', 'file_2.txt', 'out_file.txt')