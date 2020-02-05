'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
from random import randrange
import math

with open('task5_5.txt', 'w+', encoding='utf-8') as file:
    number = [randrange(100) for i in range(5)]
    summ = sum(number)
    file.write(f'Список чисел: {number} \n')
    file.write(f'Их сумма равна {summ}')