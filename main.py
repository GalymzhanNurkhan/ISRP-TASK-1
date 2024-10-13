def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число.")

def get_operation():
    while True:
        operation = input("Выберите операцию (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
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
    except ZeroDivisionError:
        return "Ошибка: деление на ноль!"

def main():
    while True:
        num1 = get_number("Введите первое число: ")
        num2 = get_number("Введите второе число: ")
        operation = get_operation()
        result = calculate(num1, num2, operation)
        print(f"Результат: {result}")
        repeat = input("Хотите выполнить другую операцию? (да/нет): ").lower()
        if repeat != 'да':
            print("Программа завершена.")
            break

if __name__ == "__main__":
    main()
