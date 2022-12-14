# -*- coding: utf-8 -*-
"""
Задание 6.6b

Сделать копию скрипта задания 6.6a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'.
Сообщение "Неправильный IP-адрес" должно выводиться только один раз после
каждого ввода адреса, даже если несколько пунктов проверки адреса не выполнены
(пример вывода ниже).

Пример выполнения скрипта:
$ python task_6_6b.py
Введите IP-адрес: 10.1.1.1
unicast

$ python task_6_6b.py
Введите IP-адрес: a.a.a
Неправильный IP-адрес
Введите IP-адрес: 10.1.1.1.1
Неправильный IP-адрес
Введите IP-адрес: 500.1.1.1
Неправильный IP-адрес
Введите IP-адрес: a.1.1.1
Неправильный IP-адрес
Введите IP-адрес: 50.1.1.1
unicast

$ python task_6_6b.py
Введите IP-адрес: 10.a.1.1.1
Неправильный IP-адрес
Введите IP-адрес: 255.255.255.255
local broadcast

"""
