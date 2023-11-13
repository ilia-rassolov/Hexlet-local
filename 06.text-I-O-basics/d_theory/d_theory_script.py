# input_file = open("input.txt", "r")
# output_file = open("output.txt", "w")
# for line in input_file:
#     for i, line in enumerate(input_file, 1):
#         output_file.write(f"{i}) {line}")
# input_file.close()
# output_file.close()




with open("input.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        for i, line in enumerate(input_file, 1):
            output_file.write(
                f"{i}) {line}"
            )