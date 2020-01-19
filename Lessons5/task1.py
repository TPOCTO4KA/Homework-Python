'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

with open ('task1_1.txt', 'w', encoding='utf-8') as f:
    while True:
        user_answer = input('введите что нибудь \n')
        if user_answer != '':
            f.write(user_answer + '\n')
        else:
            break
