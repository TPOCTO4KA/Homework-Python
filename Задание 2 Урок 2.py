'''
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()
'''

user_answer = input 'Введите список через запятую'
user_list = user_answer.split(',')  # Разделение введенного списка по заяпятой
print user_list

idx = 0  # Вводим индекс
while idx < len(user_list[:-1]):
  user_list[idx], user_list[idx+1] = user_list[idx+1], user_list[idx]
  idx += 2
print user_list
