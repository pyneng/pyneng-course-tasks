# -*- coding: utf-8 -*-
"""
Задание 9.5

Создать функцию generate_trunk_config, которая генерирует
конфигурацию для trunk-портов.

У функции должны быть такие параметры:

- intf_vlan_dict: ожидает как аргумент словарь с соответствием интерфейс-VLANы
  (пример trunk_dict)
- trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде
  списка команд (пример trunk_cmd_list)

Функция должна возвращать список команд с конфигурацией на основе указанных портов
и шаблона trunk_cmd_list. В конце строк в списке не должно быть символа
перевода строки.
Если в шаблоне trunk_template есть команда switchport trunk allowed vlan, добавить к
ней вланы указанные в словаре intf_vlan_dict.

Проверить работу функции на примере словаря trunk_dict и списка команд trunk_cmd_list.
Если предыдущая проверка прошла успешно, проверить работу функции еще раз
на словаре trunk_dict_2 и убедится, что в итоговом списке правильные номера
интерфейсов и вланов.


Пример работы функции
In [8]: generate_trunk_config(trunk_dict, trunk_cmd_list)
Out[8]:
['interface FastEthernet0/1',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 10,20,30',
 'interface FastEthernet0/2',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 11,30',
 'interface FastEthernet0/4',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 17']

In [9]: generate_trunk_config(trunk_dict_2, trunk_cmd_list)
Out[9]:
['interface FastEthernet0/11',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 120,131',
 'interface FastEthernet0/15',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 111,130',
 'interface FastEthernet0/14',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 117']


В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""

trunk_cmd_list = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_dict = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

trunk_dict_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}
