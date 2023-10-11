file_name = input("Введите имя файла: ")
line_number = int(input("Введите номер строки: "))

with open(file_name, 'r') as file:
    lines = file.readlines()

    if line_number <= 0 or line_number > len(lines):
        print("Недопустимый номер строки!")
    else:
        line = lines[line_number - 1].strip()
        print(line)