import time
a = 'FOR'
b = 'THE'
c = 'EMPEROR!'
print(a)
print(b)
print(c)
while True:
    try:
        num_1 = int(input("Хотите фокус? Введите любое число: "))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова.")
while True:
    try:
        num_2 = int(input("А еще число слабо? "))
        break
    except ValueError:
        print("Да что-ж такое-то... Попробуйте снова.")
print('А теперь ждём пару секунд. Происходит магия...')
time.sleep(5)
print(num_1)
print(num_2)
print('Та-да! Угадал же?')
