filename = input("Введите имя файла: ")
while True:
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()
        break
    except FileNotFoundError:
        filename = input("Файл не найден. Введите имя существующего файла: ")

linenumber = 0
while linenumber < 1 or linenumber > len(lines):
    try:
        linenumber = int(input("Введите номер строки: "))
        if linenumber < 1 or linenumber > len(lines):
            print("Некорректный номер строки. Попробуйте снова.")
    except ValueError:
        print("Некорректный номер строки. Попробуйте снова.")

line = linesline_number - 1
print(line)