import task_9_2
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


def test_function_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_9_2, "check_ip")


@pytest.mark.parametrize(
    "ip_address",
    ["10.1.1.250", "120.1.105.1", "130.150.1.1", "150.1.1.1"],
)
def test_task_correct_ip(ip_address):
    """
    Проверка работы задания
    """
    return_value = task_9_2.check_ip(ip_address)
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == bool
    ), f"По заданию функция должна возвращать True или False, а возвращает {type(return_value).__name__}"
    assert True == return_value, "Функция возвращает неправильное значение"


@pytest.mark.parametrize(
    "ip_address",
    ["10.1.1", "10.a.2.a", "10.1.1.1.1", "10.1.1.", "300.1.1.1", "30,1.1.1.1"],
)
def test_task_wrong_ip(ip_address):
    return_value = task_9_2.check_ip(ip_address)
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == bool
    ), f"По заданию функция должна возвращать True или False, а возвращает {type(return_value).__name__}"
    assert False == return_value, "Функция возвращает неправильное значение"
