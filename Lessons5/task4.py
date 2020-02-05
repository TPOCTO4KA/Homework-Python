'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''
from functools import reduce
my_dict = {
    'One': 'один',
    'Two': 'два',
    'Three': 'Три',
    'Four': 'Четыре'
}
new_list = []
with open('task4_4.txt', 'r', encoding='utf-8') as file_eng, open('task4_4new.txt', 'w+', encoding='utf-8') as file_rus:
    read_file = file_eng.read()
    lines = read_file.split('\n')
    for line in lines:
        new_list.append(reduce(lambda x, y: x.replace(y, my_dict[y]), my_dict, line) + '\n')
    for sub in new_list:
        file_rus.write(sub)