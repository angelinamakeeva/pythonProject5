with open('input.txt', 'r') as input_file:
    last_symbols = ''
    for line in input_file:
        last_symbol = line.strip()[-1]
        last_symbols += last_symbol
with open('output.txt', 'w') as output_file:
    output_file.write(last_symbols)