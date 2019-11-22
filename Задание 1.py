'''
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.
'''

first = 1
second = 2.5
all_numbers = f'Первое число {first}\nВторое число {second}\n'
print(all_numbers)

user_first = int(input('Введите любое первое число\n'))
user_second = int(input('Введите любое второе число\n'))
desire = input('Введите действие которое нужно произвести с этими числами\n')
if desire == 'сложение':
    sum = user_first + user_second
    print(f'Вы ввели {user_first} и {user_second}\n'
          f'{desire} этих чисел будет: {sum}')
elif desire == "вычитание":
    diff = user_first - user_second
    print(f'Вы ввели {user_first} и {user_second}\n'
          f'{desire} этих чисел будет: {diff}')
