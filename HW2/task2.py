'''
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
'''

with open('task2_2.txt', 'r', encoding='utf-8') as file:
    lines = 0  # вводим счетчики для слов и строк
    words = 0
    for line in file:  # пробегаем по строкам
        lines += 1  # суммируем их
        word = line.split()  # в новую переменную записываем список который методом split() убирает пробелы
        words += len(word)  # суммируем кол-во букв в этом списке
    print('Кол-во слов в файле: ', words)
    print('Кол-во строк в файле: ', lines)