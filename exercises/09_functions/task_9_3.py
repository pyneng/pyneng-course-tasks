# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию clean_config.

У функции clean_config должно быть два параметра:
* config_filename - ожидает как аргумент имя конфигурационного файла
* ignore_lines - ожидает как аргумент список строк, которые надо игнорировать

Функция clean_config обрабатывает конфигурационный файл и возвращает список
команд из указанного конфигурационного файла, исключая строки конфигурации,
которые начинаются с '!' и строки конфигурации в которых содержатся строки из
списка ignore_lines.
Команды в списке должны быть без перевода строки в конце строки.

Проверить работу функции на примере файла config_sw1.txt, config_sw2.txt,
config_r1.txt и списка ignore_list.

Пример работы функции:
In [2]: clean_config("config_r2_short.txt", ignore_list)
Out[2]:
['version 15.2',
 'hostname PE_r2',
 'no ip http server',
 'no ip http secure-server',
 'ip route 10.2.2.2 255.255.255.255 Tunnel0',
 'ip access-list standard LDP',
 ' deny   10.0.0.0 0.0.255.255',
 ' permit 10.0.0.0 0.255.255.255',
 'ip prefix-list TEST seq 5 permit 10.6.6.6/32',
 'mpls ldp router-id Loopback0 force',
 'control-plane',
 'alias configure sh do sh',
 'line con 0',
 ' exec-timeout 0 0',
 ' privilege level 15',
 ' logging synchronous',
 'line aux 0',
 'line vty 0 4',
 ' login',
 ' transport input all']

In [7]: clean_config("config_r2_short.txt", ["ip", "service", "line"])
Out[7]:
['Current configuration : 4052 bytes',
 'version 15.2',
 'hostname PE_r2',
 ' deny   10.0.0.0 0.0.255.255',
 ' permit 10.0.0.0 0.255.255.255',
 'mpls ldp router-id Loopback0 force',
 'control-plane',
 'alias configure sh do sh',
 'alias exec ospf sh run | s ^router ospf',
 'alias exec id show int desc',
 ' exec-timeout 0 0',
 ' privilege level 15',
 ' logging synchronous',
 ' login',
 ' transport input all']

In [8]: clean_config("config_r2_short.txt", ["ip", "service", "line", "alias"])
Out[8]:
['Current configuration : 4052 bytes',
 'version 15.2',
 'hostname PE_r2',
 ' deny   10.0.0.0 0.0.255.255',
 ' permit 10.0.0.0 0.255.255.255',
 'mpls ldp router-id Loopback0 force',
 'control-plane',
 ' exec-timeout 0 0',
 ' privilege level 15',
 ' logging synchronous',
 ' login',
 ' transport input all']


В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""

ignore_list = ["duplex", "alias exec", "Current configuration", "service"]

