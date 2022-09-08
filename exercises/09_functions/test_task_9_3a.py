import task_9_3a
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, check_function_params


def test_function_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_9_3a, "clean_config")


def test_function_params():
    """
    Проверка имен и количества параметров
    """
    check_function_params(
        function=task_9_3a.clean_config,
        param_count=5,
        param_names=[
            "config_filename",
            "ignore_lines",
            "ignore_exclamation",
            "strip_lines",
            "delete_empty_lines",
        ],
    )


def test_function_return_value_ignore_list():
    """
    Проверка работы функции
    """
    correct_return_value = [
        "hostname PE_r3",
        "!",
        "no ip http server",
        "no ip http secure-server",
        "ip route 10.2.2.2 255.255.255.255 Tunnel0",
        "!",
        "!",
        "ip prefix-list TEST seq 5 permit 10.6.6.6/32",
        "!",
        "!",
        "!",
        "alias configure sh do sh",
        "!",
        "line con 0",
        "exec-timeout 0 0",
        "privilege level 15",
        "logging synchronous",
    ]

    ignore_list = ["duplex", "alias exec", "Current configuration", "service"]
    return_value = task_9_3a.clean_config(
        "config_r3_short.txt",
        strip_lines=True,
        ignore_lines=ignore_list,
        ignore_exclamation=False,
    )
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == list
    ), f"По заданию функция должна возвращать список, а возвращает {type(return_value).__name__}"
    assert (
        correct_return_value == return_value
    ), "Функция возвращает неправильное значение"


def test_function_return_value_different_args_1():
    """
    Проверка работы функции
    """
    correct_return_value = [
        "hostname PE_r3",
        "no ip http server",
        "no ip http secure-server",
        "ip route 10.2.2.2 255.255.255.255 Tunnel0",
        "ip prefix-list TEST seq 5 permit 10.6.6.6/32",
        "alias configure sh do sh",
        "line con 0",
        "exec-timeout 0 0",
        "privilege level 15",
        "logging synchronous",
    ]

    ignore_list = ["duplex", "alias exec", "Current configuration", "service"]
    return_value = task_9_3a.clean_config(
        "config_r3_short.txt", strip_lines=True, ignore_lines=ignore_list
    )
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == list
    ), f"По заданию функция должна возвращать список, а возвращает {type(return_value).__name__}"
    assert (
        correct_return_value == return_value
    ), "Функция возвращает неправильное значение"


def test_function_return_value_different_args_2():
    """
    Проверка работы функции
    """
    correct_return_value = [
        "hostname PE_r3",
        "",
        "no ip http server",
        "no ip http secure-server",
        "ip route 10.2.2.2 255.255.255.255 Tunnel0",
        "",
        "ip prefix-list TEST seq 5 permit 10.6.6.6/32",
        "",
        "alias configure sh do sh",
        "alias exec ospf sh run | s ^router ospf",
        "alias exec bri show ip int bri | exc unass",
        "line con 0",
        "exec-timeout 0 0",
        "privilege level 15",
        "logging synchronous",
    ]

    return_value = task_9_3a.clean_config(
        "config_r3_short.txt", strip_lines=True, delete_empty_lines=False
    )
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == list
    ), f"По заданию функция должна возвращать список, а возвращает {type(return_value).__name__}"
    assert (
        correct_return_value == return_value
    ), "Функция возвращает неправильное значение"
