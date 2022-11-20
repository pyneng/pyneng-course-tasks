# -*- coding: utf-8 -*-
"""
Задание 18.2c

Скопировать функцию send_config_commands из задания 18.2b и переделать ее таким образом:

Если при выполнении команды возникла ошибка, спросить пользователя надо ли выполнять
остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды. Это значение по умолчанию,
  поэтому нажатие любой комбинации воспринимается как y
* n или no - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.

Пример работы функции:

In [11]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: y
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: n

In [12]: pprint(result)
({},
 {'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

In [12]: pprint(result, sort_dicts=False)
({},
 {'logging 0255.255.1': 'configure terminal\n'
                        'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#',
  'logging': 'logging\n% Incomplete command.\n\nR1(config)#'})


Тесты в этом разделе проверяют подключение на устройствах в файле devices.yaml.
Если параметры подключения к вашим устройствам отличаются, надо изменить
параметры в файле devices.yaml.
"""

# списки команд с ошибками и без:
commands_with_errors = ["logging 0255.255.1", "logging", "a"]
correct_commands = ["logging buffered 20010", "ip http server"]

commands = commands_with_errors + correct_commands
import re
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
import yaml
from pprint import pprint

# списки команд с ошибками и без:
commands_with_errors = ["logging 0255.255.1", "logging", "i"]
correct_commands = ["logging buffered 20010", "ip http server"]
commands = correct_commands + commands_with_errors


def send_config_commands(device, config_commands, log = True):
    correct_dict = {}
    uncorrect_dict = {}
    dev = device['host']
    error_message = 'Команда "{}" выполнилась с ошибкой "{}" на устройстве {}'
    regex = "% (?P<errmsg>.+)"
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            if log:
                print('Подключаюсь к '+dev)
            for command in config_commands:
                output= ssh.send_config_set(command)
                error_in_result = re.search(regex, output)
                if error_in_result:
                    print(error_message.format(command, error_in_result.group("errmsg"), ssh.host))
                    user_inpt = input('продолжать выполнять команды? [y]/n:') or 'y'
                    uncorrect_dict[command] = output
                    if user_inpt == 'y':
                        pass
                    elif user_inpt == 'n' or user_inpt == 'no':
                        ssh.exit_config_mode()
                        break
                else:
                    correct_dict[command] = output
                   
        return correct_dict, uncorrect_dict
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        pprint(send_config_commands(dev, commands))
