'''
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''

from itertools import count, cycle
n = int(input('Введите число = '))
stop = int(input('Введите до какого числа = '))
list1 = input('Введите список = ')
с = 0
for el in count(n):
    if el > stop:
        break
    else:
        print(el)
for el in cycle(list1):
    if с >= len(list1):
        break
    print(el)
    с += 1