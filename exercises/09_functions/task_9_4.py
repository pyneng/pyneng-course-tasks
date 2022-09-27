# -*- coding: utf-8 -*-
"""
Задание 9.4

Создать функцию generate_access_dict, которая генерирует конфигурацию
для access-портов.

У функции должно быть два параметра:
* intf_vlan_dict - ожидает как аргумент словарь с соответствием интерфейс-VLAN
  (пример access_dict)
* access_template - ожидает как аргумент список строк, которые надо добавить
  для каждого интерфейсы (пример cmd_list)

Функция должна возвращать список всех портов в режиме access с конфигурацией
на основе шаблона access_cmd_list. В конце строк в списке не должно быть
символа перевода строки.
Если в шаблоне access_template есть команда switchport access vlan, добавить к
ней номер влана указанный в словаре intf_vlan_dict

Проверить работу функции на примере словаря access_dict и списка команд
access_cmd_list.  Если предыдущая проверка прошла успешно, проверить работу
функции еще раз на словаре access_dict_2 и списке команд cmd_list и убедиться,
что в итоговом списке правильные номера интерфейсов и вланов.

Пример работы функции

In [4]: generate_access_dict(access_dict, cmd_list)
Out[4]:
['interface FastEthernet0/12',
 'switchport mode access',
 'switchport access vlan 10',
 'interface FastEthernet0/14',
 'switchport mode access',
 'switchport access vlan 11']

In [6]: generate_access_config(access_dict_2, access_cmd_list)
Out[6]:
['interface FastEthernet0/3',
 'switchport mode access',
 'switchport access vlan 100',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'interface FastEthernet0/7',
 'switchport mode access',
 'switchport access vlan 101',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'interface FastEthernet0/9',
 'switchport mode access',
 'switchport access vlan 107',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'interface FastEthernet0/10',
 'switchport mode access',
 'switchport access vlan 111',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable']


Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
access_dict = {"FastEthernet0/12": 10, "FastEthernet0/14": 11}
access_dict_2 = {
    "FastEthernet0/3": 100,
    "FastEthernet0/7": 101,
    "FastEthernet0/9": 107,
    "FastEthernet0/10": 111,
}

access_cmd_list = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]
cmd_list = ["switchport mode access", "switchport access vlan"]
