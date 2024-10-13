import math

# Словарь с операциями
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: "Ошибка: деление на ноль!" if y == 0 else x / y,
    '**': lambda x, y: x ** y,
    'sqrt': lambda x: math.sqrt(x) if x >= 0 else "Ошибка: отрицательное число!"
}

def get_number(prompt):
    """Запрос числа у пользователя."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число.")

def get_operation():
    """Запрос операции у пользователя."""
    print("Доступные операции: +, -, *, /, **, sqrt (квадратный корень)")
    while True:
        operation = input("Выберите операцию: ")
        if operation in operations:
            return operation
        print("Ошибка: некорректная операция.")

def calculate(operation, num1=None, num2=None):
    """Выполнение математической операции."""
    if operation == 'sqrt':
        return operations[operation](num1), operations[operation](num2)
    else:
        return operations[operation](num1, num2)

def main():
    """Основная логика программы."""
    while True:
        operation = get_operation()

        if operation == 'sqrt':
            num1 = get_number("Введите первое число для извлечения корня: ")
            num2 = get_number("Введите второе число для извлечения корня: ")
            result1, result2 = calculate(operation, num1, num2)
            print(f"Квадратный корень из {num1}: {result1}")
            print(f"Квадратный корень из {num2}: {result2}")
        else:
            num1 = get_number("Введите первое число: ")
            num2 = get_number("Введите второе число: ")
            result = calculate(operation, num1, num2)
            print(f"Результат: {result}")

        repeat = input("Хотите выполнить другую операцию? (да/нет): ").lower()
        if repeat != 'да':
            print("Программа завершена.")
            break

if __name__ == "__main__":
    main()
