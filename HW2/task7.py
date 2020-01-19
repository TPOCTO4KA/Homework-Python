'''
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

import json
report = {}
aver_profit = 0
with open('task7_7.txt', 'r', encoding='utf-8') as base:
    read_file = base.read()
    lines = read_file.split('\n')
    for line in lines:
        name, own, revenue, costs = line.split()
        profit = float(revenue) - float(costs)
        print(f'Прибыль компании {name} составляет {profit}')
        report.update({name : profit})
        if profit >= 0:
            aver_profit += profit
        aver_profit /= len(lines)
report['Средняя прибыль'] = aver_profit

with open("firm.json", "w") as f_json:
    json.dump(report, f_json)