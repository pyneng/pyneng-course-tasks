try:
    import task_11_1a
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
    check_function_exists(task_11_1a, "convert_mac_list")


@pytest.mark.parametrize(
    "mac_list,correct_converted_mac_list",
    [
        (
            ["1a1b.2c2d.3e3f", "aaaabbbbcccc"],
            ["1a:1b:2c:2d:3e:3f", "aa:aa:bb:bb:cc:cc"],
        ),
        (
            ["1111:2222:3333", "1a-1b-2c-2d-3e-3f"],
            ["11:11:22:22:33:33", "1a:1b:2c:2d:3e:3f"],
        ),
    ],
)
def test_function_return_value_correct_mac(mac_list, correct_converted_mac_list):
    """
    Проверка работы функции
    """

    return_value = task_11_1a.convert_mac_list(mac_list)
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == list
    ), f"По заданию функция должна возвращать список, а возвращает {type(return_value).__name__}"
    assert (
        correct_converted_mac_list == return_value
    ), (
        f"Функция возвращает неправильное значение.\nЕсли функции передается "
        f"как аргумент список {mac_list},\nрезультат должен быть {correct_converted_mac_list}"
    )


@pytest.mark.parametrize(
    "wrong_mac_list",
    [
        ["1a.2c2d.3e3f", "1a1b.2c2d.3e3f"],
        ["1111:2222:3333", "aaaabbRRcccc"],
        ["1111:2222:333333", "11:11:22:22:33:33"],
        ["1a-1b-2c-2d-3e-3f-aa"],
    ],
)
def test_function_return_value_wrong_mac_strict_true(wrong_mac_list):
    """
    Проверка работы функции с неправильными MAC-адресам
    """
    with pytest.raises(ValueError) as excinfo:
        return_value = task_11_1a.convert_mac_list(wrong_mac_list, strict=True)


@pytest.mark.parametrize(
    "mac_list,correct_converted_mac_list",
    [
        (
            ["1a1b.WWWW.3e3f", "aaaabbbbcccc"],
            ["aa:aa:bb:bb:cc:cc"],
        ),
        (
            ["1111:2222:33", "1a-1b-2c-2d-3e-3f"],
            ["1a:1b:2c:2d:3e:3f"],
        ),
    ],
)
def test_function_return_value_wrong_mac_strict_false(
    mac_list, correct_converted_mac_list
):
    """
    Проверка работы функции
    """
    return_value = task_11_1a.convert_mac_list(mac_list, strict=False)
    assert (
        correct_converted_mac_list == return_value
    ), (
        f"Функция возвращает неправильное значение.\nЕсли функции передается "
        f"как аргумент список {mac_list},\nрезультат должен быть {correct_converted_mac_list}"
    )
