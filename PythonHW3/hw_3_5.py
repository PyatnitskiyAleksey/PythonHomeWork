"""""
Программа запрашивает у пользователя строку чисел, разделённых пробелом. 
При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. 
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел 
к полученной ранее сумме и после этого завершить программу.
"""""

def summa ():
    n = 0
    q = False
    while q == False:
            try:
                entered_list = input("Введите список чисел, разделенных пробелом. Для выхода из программы нажмите q: ").split()
                res = 0
                for el in range(len(entered_list)):
                    if entered_list[el] == 'q' or entered_list[el] == 'Q':
                        q = True
                        print('Выход из программы')
                        break
                    else:
                        res = res + int(entered_list[el])
                n = n + res
                print(f'Сумма списка {n}')
                print(f'Накопление сумм списка {n}')
            except ValueError:
                print('ERROR')
                print(n)
summa()


"""""""""
n = 0
entered_list = 0
while True:
    try:
        entered_list = input("Введите список чисел, разделенных пробелом. Для выхода из программы нажмите q: ").split()
        num_list = list(map(int, entered_list))
        n = n + sum(num_list)
        print("Список введенных чисел: ", num_list)
        print("Сумма списка:", sum(num_list))
        print("Накопление сумм списка:", n)
    except ValueError:
        print('ERROR')
        print(n)
        if 'q' in entered_list: #Срабаывает отдельно на q
            break
        #Нет суммы до q. А вариант был неплох...


"""""