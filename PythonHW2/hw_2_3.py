""""""""""
Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и dict. 
"""""""""""

month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
diction_year = {0: 'Зима', 1: 'Весна', 2: 'Лето',  3: 'Осень', 4: 'Зима'} # словарь
n = int(input("Введите месяц в виде целого числа от 1 до 12: "))
while 0 < n and n <= 12:
    print('Месяц под номером', n, '- это', month[n-1], ', относится ко времени года:', diction_year.get(int(n) // 3))
    break
else:
    print('ERROR!')



