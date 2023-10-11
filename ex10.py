with open('simple/inputex10.txt', 'r') as input_file:
    with open('simple/outputex10.txt', 'w') as output_file:
        lines = input_file.readlines()
        for i, line in enumerate(lines):
            if i % 2 == 1:
                output_file.write(line)
