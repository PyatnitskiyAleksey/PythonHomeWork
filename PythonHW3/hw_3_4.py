"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""
x = int(input('Введите положительное целое число x:'))
while x < 0:
    try:
        x = int(input('Неправильно! Полжительное целое число x:'))
    except ValueError:
        x = int(input('Неправильно! Полжительное целое число x:'))
y = int(input('Введите отрицательное целое число у:'))
while y >= 0:
    try:
        y = int(input('Неправильно! Отрицательное целое число y:'))
    except ValueError:
        y = int(input('Неправильно! Отрицательное целое число y:'))

def res(x, y): #Первый способ — возведение в степень с помощью оператора **.
    q = x**y
    return q
print(f'Ответ по первому способу решения - {float(res(x, y))}')

#Второй способ — возведение в степень с помощью цикла.
def res(x, y):
    x1 = 1
    for y in range(0, abs(y)):
        x1 = x1 * x
    q=1/x1
    return q
print(f'Ответ по второму способу решения - {float(res(x, y))}')
