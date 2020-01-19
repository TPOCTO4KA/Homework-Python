'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

with open('task3_3', 'r', encoding='utf-8') as file:
    users = file.readlines()
    name = []
    solary = []
    for i in users:
        name.append([el for el in i.split()][0])
        solary.append([el for el in i.split()][1])
    my_dict = dict(zip(name, solary))
    print(my_dict)
    print('Меньше 20 тысяч получают: ', [key for key, value in my_dict.items() if int(value) <= 20000])
    print('Средняя величина Дохода: ', dict(zip(name, [(int(value) * 12) // 19.5 for key, value in my_dict.items()])))