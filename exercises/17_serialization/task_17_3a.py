# -*- coding: utf-8 -*-
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод
команды show cdp neighbor из нескольких файлов и записывает итоговую
топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами,
независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь
в файл topology.yaml. Он понадобится в следующем задании.

Пример вызова функции
In [11]: pprint(generate_topology_from_cdp(["sh_cdp_n_sw1.txt", "sh_cdp_n_r1.txt"]), sort_dicts=False)
{'SW1': {'Eth 0/1': {'R1': 'Eth 0/0'},
         'Eth 0/2': {'R2': 'Eth 0/0'},
         'Eth 0/3': {'R3': 'Eth 0/0'},
         'Eth 0/4': {'R4': 'Eth 0/0'}},
 'R1': {'Eth 0/0': {'SW1': 'Eth 0/1'}}}

In [12]: f_list
Out[12]:
['sh_cdp_n_r2.txt',
 'sh_cdp_n_r5.txt',
 'sh_cdp_n_r1.txt',
 'sh_cdp_n_sw1.txt',
 'sh_cdp_n_r3.txt',
 'sh_cdp_n_r4.txt',
 'sh_cdp_n_r6.txt']

In [13]: pprint(generate_topology_from_cdp(f_list), sort_dicts=False)
{'R2': {'Eth 0/0': {'SW1': 'Eth 0/2'},
        'Eth 0/1': {'R5': 'Eth 0/0'},
        'Eth 0/2': {'R6': 'Eth 0/1'}},
 'R5': {'Eth 0/0': {'R2': 'Eth 0/1'}, 'Eth 0/1': {'R4': 'Eth 0/1'}},
 'R1': {'Eth 0/0': {'SW1': 'Eth 0/1'}},
 'SW1': {'Eth 0/1': {'R1': 'Eth 0/0'},
         'Eth 0/2': {'R2': 'Eth 0/0'},
         'Eth 0/3': {'R3': 'Eth 0/0'},
         'Eth 0/4': {'R4': 'Eth 0/0'}},
 'R3': {'Eth 0/0': {'SW1': 'Eth 0/3'}},
 'R4': {'Eth 0/0': {'SW1': 'Eth 0/4'}, 'Eth 0/1': {'R5': 'Eth 0/1'}},
 'R6': {'Eth 0/1': {'R2': 'Eth 0/2'}}}
"""
