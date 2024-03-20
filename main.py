"""
Программа калькулятор...
"""


def calc_info():
    print('Калькулятор работает только с [+, -, *, /]!!!')


def input_operation():
    operations = ('+', '-', '*', '/')
    while True:
        operation = input('Введите операцию: ')

        if operation not in operations:
            print('Калькулятор не работает с этой операцией, повторите...')
            continue

        break

    return operation


def input_number(step):
    while True:
        number = input(f'Введите {step} число: ')

        if not number.isdigit():
            print('Введите число, повторите!!!')
            continue

        break

    return float(number)


def solve(number_one, number_two, operation):
    result = None

    if operation == '+':
        result = number_one + number_two
    elif operation == '-':
        result = number_one - number_two
    elif operation == '*':
        result = number_one * number_two
    else:
        result = number_one / number_two

    return result


def print_solve(number_one, number_two, operation, result):
    print(f'{number_one} {operation} {number_two} = {result}')


def main():
    calc_info()
    number_one = input_number('первое')
    number_two = input_number('второе')
    operation = input_operation()
    result = solve(number_one, number_two, operation)
    print_solve(number_one, number_two, operation, result)


if __name__ == '__main__':
    main()
