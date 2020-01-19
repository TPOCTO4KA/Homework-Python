'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
import re
my_dict = {}
with open('task6_6.txt', 'r', encoding='utf-8') as base:
    subj = {}  # пустой словарь для записи
    for line in base:  # проход по строкам файла
        subject, lecture, practical, lab = line.split()  # разбиваем строки на ключ-subject, значение-lec, pra ,lab
        subj[subject] = sum(float(i) for i in re.findall(r'\d+', lecture + practical + lab))  # собираем словарь по ключу.
        # re.findall(r'\d+', lecture + practical + lab) из этого выражения вытаскиваем циферки и суммируем значения, записываем в value
    print(subj)