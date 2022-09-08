from importlib import reload
import sys
import pytest


@pytest.mark.parametrize("index,correct_word", [("0", "guido"), ("5", "on"), ("6", "python")])
def test_task_sw1(capsys, monkeypatch, index, correct_word):
    """
    Проверка работы задания при вводе sw1
    """
    monkeypatch.setattr("builtins.input", lambda x=None: index)
    if sys.modules.get("task_5_1"):
        reload(sys.modules["task_5_1"])
    import task_5_1

    out, err = capsys.readouterr()
    assert out, (
        "Ничего не выведено на стандартный поток вывода. Надо не только получить "
        "нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    )
    assert (
        correct_word in out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"
