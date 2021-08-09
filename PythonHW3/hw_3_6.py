"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""

def int_func(says):
    english = 'qwertyuiopasdfghjklzxcvbnm'
    return says.title() if not set(says).difference(english) else False # Возвратить текст с заглавного символа,
                                                                    # если в наборе нет отличий от словаря.

Samuel_L_Jackson = input('English MF do you speak it?: ').split
for s in Samuel_L_Jackson():
    res = int_func(s)
    if res:
        print(int_func(s), ' ')
