try:
    import task_11_1
except OSError:
    pytest.fail(
        "Для этого задания функцию надо ОБЯЗАТЕЛЬНО вызывать в блоке if __name__ == '__main__':"
    )

import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


def test_function_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_11_1, "convert_mac")


@pytest.mark.parametrize(
    "mac,correct_converted_mac",
    [
        ("aaaabbbbcccc", "aa:aa:bb:bb:cc:cc"),
        ("1111:2222:3333", "11:11:22:22:33:33"),
        ("1a1b.2c2d.3e3f", "1a:1b:2c:2d:3e:3f"),
        ("1111.2222.3333", "11:11:22:22:33:33"),
        ("1111-2222-3333", "11:11:22:22:33:33"),
    ],
    ids=str,
)
def test_function_return_value_correct_mac(mac, correct_converted_mac):
    """
    Проверка работы функции
    """

    return_value = task_11_1.convert_mac(mac)
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == str
    ), f"По заданию функция должна возвращать строку, а возвращает {type(return_value).__name__}"
    assert (
        correct_converted_mac == return_value
    ), "Функция возвращает неправильное значение"


@pytest.mark.parametrize(
    "wrong_mac",
    [
        "1a.2c2d.3e3f",
        "aaaabbttcccc",
        "1111:2222:333333",
        "1111:KK22:3333",
    ],
)
def test_function_return_value_wrong_mac(wrong_mac):
    """
    Проверка работы функции с неправильными MAC-адресам
    """
    with pytest.raises(ValueError) as excinfo:
        return_value = task_11_1.convert_mac(wrong_mac)
