'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''
from random import choice

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police  # Должна быть True False

    def go(self):
        print(f'Машина {self.name}, {self.color} цвета, поехала')

    def stop(self):
        print(f'{self.name}, {self.color} цвета, остановилась')

    def turn(self):  # Добавить указание стороны поворота
        dest = choice(("left", "right"))
        print(f'Машина {self.name}, {self.color} цвета, повернула {dest}')

    def show_speed(self):  # Для показывания текущей скорости
        print(f'Машина {self.name}, {self.color} цвета, едет со скоростью {self.speed} км/ч')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Машина {self.name}, {self.color} цвет')
        if self.speed >= 60:
            print(f'{self.name} привысил скорость')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Машина {self.name}, {self.color} цвет')
        if self.speed >= 40:
            print(f'{self.name} привысил скорость')

class Police(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car1 = SportCar(100, 'blue', 'mazda', False)
car1.go()
car1.stop()
car1.turn()
car1.show_speed()