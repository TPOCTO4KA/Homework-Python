'''
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

n = input('Введите n = ')
first_n = int(n)
second_n = int(f'{n}{n}')
third_n = int(f'{n}{n}{n}')
summ = first_n + second_n + third_n
print(summ)
