# -*- coding: utf-8 -*-
"""
Задание 7.5

Создать скрипт, который будет обрабатывать конфигурационный файл коммутатора и
получать из него информацию о конфигурации интерфейсов.

Имя файла конфигурации передается как аргумент скрипту.
$ python task_7_5.py config_trunk_sw2.txt
$ python task_7_5.py config_trunk_sw3.txt

Передавать имя файла как аргумент скрипту. Указанный конфиг надо обработать и
получить словарь где ключи имя интерфейса, а значение список команд, которые
начинаются на switchport. Команды в списке должны быть без пробела в начале
строки и перевода строки в конце.

Записать итоговый словарь в переменную interface_dict (именно эта переменная будет
проверяться в тесте). По желанию можно выводить словарь на экран, тест
проверяет только содержимое переменной. Тут удобно выводить словарь с помощью pprint.

Например, для файла config_trunk_sw2.txt должен получиться такой словарь:

$ python task_7_5.py config_trunk_sw2.txt
{'FastEthernet0/1': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 100,200',
                     'switchport mode trunk'],
 'FastEthernet0/2': ['switchport mode access',
                     'switchport access vlan 20'],
 'FastEthernet0/3': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 100,300,400,500,600',
                     'switchport mode trunk'],
 'FastEthernet0/4': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 400,500,600',
                     'switchport mode trunk'],
 'FastEthernet0/5': ['switchport mode access',
                     'switchport access vlan 30'],
 'FastEthernet0/6': ['switchport mode access',
                     'switchport access vlan 20']}

Для файла config_trunk_sw3.txt должен получиться такой словарь:
$ python task_7_5.py config_trunk_sw3.txt
{'FastEthernet0/1': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 10,20,21,22',
                     'switchport mode trunk'],
 'FastEthernet0/2': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 10,13,1450,1451,1452',
                     'switchport mode trunk'],
 'FastEthernet0/3': ['switchport mode access',
                     'switchport access vlan 20'],
 'FastEthernet0/4': ['switchport mode access',
                     'switchport access vlan 20'],
 'FastEthernet0/5': ['switchport mode access',
                     'switchport access vlan 30'],
 'FastEthernet0/6': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 40,50,60',
                     'switchport mode trunk'],
 'FastEthernet0/7': ['switchport mode access'],
 'FastEthernet0/8': ['switchport mode access']}

Проверить работу функции на примере файлов config_trunk_sw2.txt и config_trunk_sw3.txt.
Убедиться, что для этих файлов получаются правильные словари.

"""
from pprint import pprint
