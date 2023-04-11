def calculator(usr, a, b):
    if usr == '+':
        c = a + b
        return c
    elif usr == '-':
        c = a - b
        return c
    if usr == '*':
        c = a * b
        return c
    elif usr == '/':
        try:
            c = a / b
        except ZeroDivisionError:
            return 'Ноль Не делается'
    if usr == '**':
        c = a ** b
        return c
    elif usr == '//':
        c = a // b
        return c
    if usr == '%':
        c = a % b
        return c
    if usr == '++':
        c = float(input('Введите Трейти Число:>> '))
        d = float(input('Введите Четвертый Число:>> '))
        e = a + b + c + d
        return e
    elif usr == '--':
        c = float(input('Введите Трейти Число:>> '))
        d = float(input('Введите Четвертый Число:>> '))
        e = a - b - c - d
        return e
    else:
        return 'Не верная комманда'

if __name__ == '__main__':
    usr = input('Введите комманд (+, -, *, /, **, //, %, ++, --):>> ')
    a = float(input("Введите Первый Число:>> "))
    b = float(input('Введите Второй Число:>> '))
    print(calculator(usr, a, b))
