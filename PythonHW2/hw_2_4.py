'''''
Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. Строки нужно пронумеровать. 
Если слово длинное, выводить только первые 10 букв в слове.
'''''

letter = input('Введите пару слов: ').split()
for n, txt in enumerate(letter, 1):
    print(n, txt[:10])