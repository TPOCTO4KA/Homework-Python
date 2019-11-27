'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
a = input('введите число a ')
b = input('введите число b ')
def mucn(a, b):
    if a.isdigit() and b.isdigit():
        if a == '0' or b == '0':
            print('На ноль делить нельзя')
        else:
            a = int(a)
            b = int(b)
            def func(a, b):
                result = a // b
                return result
            result = func(a, b)
            print(f'деление равно {result}')
    else:
        print('Введены не правильные значения')
mucn(a, b)
