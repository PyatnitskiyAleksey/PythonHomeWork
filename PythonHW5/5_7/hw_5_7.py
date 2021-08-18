""""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

with open('text.txt', 'r', encoding='utf-8') as file:
    stat = []
    prof = {}
    av_prof = {}
    av = 0
    pr = 0
    i = 3
    for line in file:
        firm, own, earn, cost = line.split()
        profit = int(earn) - int(cost)
        if profit >= 0:
            pr = pr + profit
        else:
            i -= 1
        prof[firm] = profit
    stat.append(prof)
    if i != 0:
        av = pr / i
        av_prof['average_profit'] = round(av)
        stat.append(av_prof)
    else:
        print('Все компании работают в убыток')
    print(stat)
with open('file.json', 'a+', encoding='utf-8') as json_file:
    json.dump(stat, json_file)
