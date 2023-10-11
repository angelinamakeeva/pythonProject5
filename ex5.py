filename = input("Введите имя файла: ")
while True:
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()
        break
    except FileNotFoundError:
        filename = input("Файл не найден. Введите имя существующего файла: ")

linenumber = int(input("Введите номер строки: "))

try:
    line = lines[linenumber - 1]
    print(line)
except IndexError:
    print("Строка с таким номером нет")