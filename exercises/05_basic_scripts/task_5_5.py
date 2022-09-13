# -*- coding: utf-8 -*-
"""
Задание 5.5

Скрипт должен запрашивать у пользователя (в таком порядке):
* информацию о режиме интерфейса (access/trunk)
* номере интерфейса (тип и номер, вида Gi0/3)
* номер VLANа (для режима trunk будет вводиться список VLANов)

В зависимости от выбранного режима, на стандартный поток вывода, должна возвращаться
соответствующая конфигурация access или trunk (шаблоны команд находятся в переменных
access_template и trunk_template).

При этом, сначала должна идти строка interface и подставлен номер интерфейса, а затем
соответствующий шаблон, в который подставлен номер VLANа (или список VLANов).

Плюсом будет решить задание без использования условия if и цикла for,
но первый вариант решения лучше сделать так, как будет получаться.

Подсказка: в некоторых случаях словари можно использовать как замену if/elif/else.

Ниже примеры выполнения скрипта, чтобы было проще понять задачу.

Пример выполнения скрипта, при выборе режима access:

$ python task_5_5.py
Введите режим работы интерфейса (access/trunk): access
Введите тип и номер интерфейса: Fa0/6
Введите номер влан(ов): 3

interface Fa0/6
switchport mode access
switchport access vlan 3
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable

Пример выполнения скрипта, при выборе режима trunk:
$ python task_5_5.py
Введите режим работы интерфейса (access/trunk): trunk
Введите тип и номер интерфейса: Fa0/7
Введите номер влан(ов): 2,3,4,5

interface Fa0/7
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 2,3,4,5

"""

access_template = """switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
"""

trunk_template = """switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan {}
"""
