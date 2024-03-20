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

    return number


def main():
    calc_info()
    number_one = input_number('первое')
    number_two = input_number('второе')
    operation = input_operation()
    print(f'{number_one} {operation} {number_two} = результат')


if __name__ == '__main__':
    main()
