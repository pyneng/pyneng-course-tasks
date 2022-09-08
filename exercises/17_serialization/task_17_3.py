# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Пример вызова функции
In [8]: with open("sh_cdp_n_sw1.txt") as f:
   ...:     pprint(parse_sh_cdp_neighbors(f.read()), sort_dicts=False)
   ...:
{'SW1': {'Eth 0/1': {'R1': 'Eth 0/0'},
         'Eth 0/2': {'R2': 'Eth 0/0'},
         'Eth 0/3': {'R3': 'Eth 0/0'},
         'Eth 0/4': {'R4': 'Eth 0/0'}}}

In [9]: with open("sh_cdp_n_r1.txt") as f:
   ...:     pprint(parse_sh_cdp_neighbors(f.read()), sort_dicts=False)
   ...:
{'R1': {'Eth 0/0': {'SW1': 'Eth 0/1'}}}

In [10]: with open("sh_cdp_n_r2.txt") as f:
    ...:     pprint(parse_sh_cdp_neighbors(f.read()), sort_dicts=False)
    ...:
{'R2': {'Eth 0/0': {'SW1': 'Eth 0/2'},
        'Eth 0/1': {'R5': 'Eth 0/0'},
        'Eth 0/2': {'R6': 'Eth 0/1'}}}
"""
