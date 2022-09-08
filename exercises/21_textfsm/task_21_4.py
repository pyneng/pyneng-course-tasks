# -*- coding: utf-8 -*-
"""
Задание 21.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show
с помощью netmiko, а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br
и устройствах из devices.yaml.

Пример вызова функции
In [17]: result = send_and_parse_show_command(
    ...:     devices[1], "sh ip int br", templates_path=full_pth
    ...: )
    ...: pprint(result, width=120)
    ...:
[{'address': '192.168.100.2', 'intf': 'Ethernet0/0', 'protocol': 'up', 'status': 'up'},
 {'address': '10.100.23.2', 'intf': 'Ethernet0/1', 'protocol': 'up', 'status': 'up'},
 {'address': 'unassigned', 'intf': 'Ethernet0/2', 'protocol': 'down', 'status': 'administratively down'},
 {'address': 'unassigned', 'intf': 'Ethernet0/3', 'protocol': 'down', 'status': 'administratively down'},
 {'address': '10.2.2.2', 'intf': 'Loopback0', 'protocol': 'up', 'status': 'up'},
 {'address': 'unassigned', 'intf': 'Loopback9', 'protocol': 'up', 'status': 'up'},
 {'address': 'unassigned', 'intf': 'Loopback19', 'protocol': 'up', 'status': 'up'},
 {'address': '10.100.100.2', 'intf': 'Loopback100', 'protocol': 'up', 'status': 'up'},
 {'address': '10.255.1.2', 'intf': 'Tunnel2', 'protocol': 'down', 'status': 'up'}]

"""
