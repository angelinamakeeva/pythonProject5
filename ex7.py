try:
    with open('input.txt', 'r') as input_file:
        numbers = input_file.readline().split()
        number1 = int(numbers[0])
        number2 = int(numbers[1])
        number3 = int(numbers[2])
        result = number1 / number2 + number3

        with open('output.txt', 'w') as outputfile:
            outputfile.write(str(result))
except ValueError:
    print("Ошибка: некорректный формат чисел в файле input.txt")
except ZeroDivisionError:
    print("Ошибка: деление на ноль")