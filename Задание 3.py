'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
'''
my_list = []
my_list.append(int(input('Введите a\n')))
my_list.append(int(input('Введите b\n')))
my_list.append(int(input('Введите c\n')))

def my_func(my_list):
    for itm in my_list:
        number = min(my_list)
        my_list.remove(number)
        break
    end = sum(my_list)
    return end

print(my_func(my_list))