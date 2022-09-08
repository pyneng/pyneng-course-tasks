import pytest
from importlib import reload
import re
import sys

sys.path.append("..")

from pyneng_common_functions import count_calls


@count_calls
def monkey_input_number_5(prompt):
    __tracebackhide__ = True
    if monkey_input_number_5.total_calls == 1:
        return "3"
    elif monkey_input_number_5.total_calls == 2:
        return "8"
    elif monkey_input_number_5.total_calls == 3:
        return "5"
    else:
        pytest.fail(
            "Запрос чисел у пользователя должен остановиться после того как "
            "было введено правильное число"
        )


@count_calls
def monkey_input_number_8(prompt):
    __tracebackhide__ = True
    if monkey_input_number_8.total_calls == 1:
        return "7"
    elif monkey_input_number_8.total_calls == 2:
        return "8"
    else:
        pytest.fail(
            "Запрос чисел у пользователя должен остановиться после того как "
            "было введено правильное число"
        )


def test_task_random_5_input_3_8_5(capsys, monkeypatch):
    """
    Проверка работы задания при задуманном числе 5 и вводе 3, 8, 5
    """
    monkeypatch.setattr("random.randint", lambda x, y: 5)
    monkeypatch.setattr("builtins.input", monkey_input_number_5)
    import task_6_5

    correct_stdout = (
        "\nВведите число: 3\n"
        "Задуманное число больше\n"
        "Введите число: 8\n"
        "Задуманное число меньше\n"
        "Введите число: 5\n"
        "Правильно!\n"
    )
    out, err = capsys.readouterr()
    out = out.strip().lower()
    assert out, "Ничего не выведено на стандартный поток вывода."
    assert "больше" in out and "меньше" in out and "правильно" in out, (
        f"При задуманном числе 5 и вводе пользователя 3, 8, 5, на стандартном "
        f"потоке вывода должен быть такой вывод {correct_stdout}"
    )


def test_task_random_8_input_7_8(capsys, monkeypatch):
    """
    Проверка работы задания при задуманном числе 8 и вводе 7, 8
    """
    monkeypatch.setattr("random.randint", lambda x, y: 8)
    monkeypatch.setattr("builtins.input", monkey_input_number_8)
    if sys.modules.get("task_6_5"):
        reload(sys.modules["task_6_5"])
    import task_6_5

    correct_stdout = (
        "\nВведите число: 7\n"
        "Задуманное число больше\n"
        "Введите число: 8\n"
        "Правильно!\n"
    )
    out, err = capsys.readouterr()
    out = out.strip().lower()
    assert out, "Ничего не выведено на стандартный поток вывода."
    assert "больше" in out and "правильно" in out, (
        f"При задуманном числе 8 и вводе пользователя 7, 8 на стандартном "
        f"потоке вывода должен быть такой вывод {correct_stdout}"
    )


def test_task_random_4_input_1_1_1_1_1(capsys, monkeypatch):
    """
    Проверка работы задания при задуманном числе 4 и вводе 1, 1, 1, 1, 1
    """
    monkeypatch.setattr("random.randint", lambda x, y: 4)
    monkeypatch.setattr("builtins.input", lambda x: "1")
    if sys.modules.get("task_6_5"):
        reload(sys.modules["task_6_5"])
    import task_6_5

    correct_stdout = (
        "\nВведите число: 1\n"
        "Задуманное число больше\n"
        "\nВведите число: 1\n"
        "Задуманное число больше\n"
        "\nВведите число: 1\n"
        "Задуманное число больше\n"
        "\nВведите число: 1\n"
        "Задуманное число больше\n"
        "\nВведите число: 1\n"
        "Задуманное число больше\n"
        "Число не угадано после 5 попыток\n"
    )
    out, err = capsys.readouterr()
    assert out, "Ничего не выведено на стандартный поток вывода."
    assert out.lower().count("больше") == 5 and "не угадано" in out.lower(), (
        f"При задуманном числе 8 и вводе пользователя 1, 1, 1, 1, 1 на стандартном "
        f"потоке вывода должен быть такой вывод {correct_stdout}"
    )
