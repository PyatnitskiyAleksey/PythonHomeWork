"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv
def zarplata():
    try:
        hour, cost, bonus = map(float, argv[1:])
        print(f'Зарплата: {hour * cost + bonus}')
    except ValueError:
        print("ERROR!")
zarplata()