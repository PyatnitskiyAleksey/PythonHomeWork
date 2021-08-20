"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery():

    def __init__(self, title):
        self.title = title

    def draw(self):
        return ('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        return (f'Рисуется тонкая линия {self.title}.')

class Pencil(Stationery):
    def draw(self):
        return (f'Рисуется линия {self.title}.')

class Handle(Stationery):
    def draw(self):
        return (f'Рисуется жирная линия {self.title}.')

pen = Pen("Черная ручка")
print(pen.draw())

pencil = Pencil("Черный карандаш")
print(pencil.draw())

handle = Handle("Синий маркер")
print(handle.draw())

