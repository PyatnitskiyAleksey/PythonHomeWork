"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

class Road():

    def __init__(self, lenght, wight):
        self._lenght = lenght
        self._wight = wight
        self.weight = 25
        self.height = 5

    def mass(self):
        weight = self._lenght * self._wight * self.weight * self.height
        print(
            f'Масса асфальта для покрытия одного кв.метра дороги асфальтом,толщиной в 1 см, '
            f'принимается равной {self.weight} кг.\n'
            f'Толщина полотна принимается равной {self.height} см.')
        print(f'Необходимая масса асфальта для покрытия дороги длиной {self._lenght} м, шириной {self._wight} м '
              f'равно {round(weight) / 1000} тонн')

r = Road(10000, 15)

r.mass()





