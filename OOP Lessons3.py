'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker():
    _income = {
        'wage': 0,
        'bonus': 0
    }

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника - {self.surname} {self.name} \nДолжность - {self.position}')

    def get_total_income(self):
        total = sum(self._income.values())
        print(f'Доход сотрудника {total}')


pers1 = Position('Kirill', 'Lukyanov', 'Buisness Analist', 90000, 150000)
pers1.get_full_name()
pers1.get_total_income()
