# -*- coding: utf-8 -*-
"""
Задание 7.2a

Создать скрипт, который будет обрабатывать конфигурационный файл коммутатора и
выводить на экран строки из конфига, исключая некоторые.

Имя файла конфигурации передается как аргумент скрипту.
$ python task_7_2a.py config_sw1.txt

Вывести на стандартный поток вывода команды из переданного конфигурационного
файла, исключая строки, которые начинаются с '!' и строки в которых содержатся
слова из списка ignore.
Вывод не должен содержать пустые строки.

Пример вывода:
$ python task_7_2a.py config_sw1.txt
version 15.0
hostname sw1
interface Ethernet0/0
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 spanning-tree portfast edge trunk
interface Ethernet0/2
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 spanning-tree portfast edge trunk
interface Ethernet1/0
interface Ethernet1/1
interface Ethernet1/2
interface Ethernet1/3
interface Vlan100
 ip address 10.0.100.1 255.255.255.0
line con 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
line aux 0
line vty 0 4
 login
 transport input all

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

"""

ignore = ["duplex", "alias", "configuration", "end", "service"]
