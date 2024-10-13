import math


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число.")


def get_operation():
    operations = {
        '+': 'сложение',
        '-': 'вычитание',
        '*': 'умножение',
        '/': 'деление',
        '**': 'возведение в степень',
        'sqrt': 'квадратный корень'
    }
    print("Доступные операции:")
    for symbol, name in operations.items():
        print(f"{symbol} - {name}")

    while True:
        operation = input("Выберите операцию: ")
        if operation in operations:
            return operation
        print("Ошибка: некорректная операция.")


def calculate(num1, num2, operation):
    try:
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            return num1 / num2
        elif operation == '**':
            return num1 ** num2
        elif operation == 'sqrt':
            return math.sqrt(num1), math.sqrt(num2)
    except ZeroDivisionError:
        return "Ошибка: деление на ноль!"
    except ValueError:
        return "Ошибка: невозможно извлечь корень из отрицательного числа!"


def main():
    while True:
        operation = get_operation()

        if operation == 'sqrt':
            num1 = get_number("Введите первое число для извлечения корня: ")
            num2 = get_number("Введите второе число для извлечения корня: ")
            result1, result2 = calculate(num1, num2, operation)
            print(f"Квадратный корень из {num1}: {result1}")
            print(f"Квадратный корень из {num2}: {result2}")
        else:
            num1 = get_number("Введите первое число: ")
            num2 = get_number("Введите второе число: ")
            result = calculate(num1, num2, operation)
            print(f"Результат: {result}")

        repeat = input("Хотите выполнить другую операцию? (да/нет): ").lower()
        if repeat != 'да':
            print("Программа завершена.")
            break


if __name__ == "__main__":
    main()
