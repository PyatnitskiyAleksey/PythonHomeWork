"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
class Car():

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return (f'{self.name} поехала. ')

    def stop(self):
        return (f'{self.name} остановилась. ')

    def turn(self, direction):
        return (f'{self.name} повернула {direction}. ')

    def show_speed(self):
        return (f'Скорость движения {self.speed}. ')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return (f'Сбавь скорость! Ты двигаешься со скоростью {self.speed}! ')
        else:
            return (f'Скорость движения {self.speed}. ')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return (f'Сбавь скорость! Ты двигаешься со скоростью {self.speed}! ')
        else:
            return (f'Скорость движения {self.speed}. ')

class PoliceCar(Car):
    pass

town = TownCar(70, 'синяя', 'Audi', False)
print(town.go(), town.show_speed(), town.turn('Налево'), town.turn('Направо'), town.stop())

sport = SportCar(170, 'red', 'RS3', False)
print(sport.go(), sport.show_speed(), sport.turn('Налево'), sport.stop())

work = WorkCar(35, 'фиолетовый', 'ПАЗик', False)
print(work.go(), work.show_speed(), work.turn('Направо'), work.stop())

police = PoliceCar(100, 'LGBT', 'УАЗик типа Бобик', True)
print(police.go(), police.show_speed(), police.turn('Направо'), police.stop())

