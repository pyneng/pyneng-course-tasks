def test_task_stdout(capsys):
    """
    Проверка работы задания
    """
    import task_6_2

    out, err = capsys.readouterr()
    correct_stdout = (
        "GUIdO vAn ROssUm bEgAn wOrkIng On PYthOn In thE lAtE 1980s"
    )
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout == out.strip()
    ), "На стандартный поток вывода выводится неправильная строка"


def test_task_variables():
    """
    Проверка что в задании создана нужная переменная
    и в ней содержится правильный результат
    """
    import task_6_2

    # переменные созданные в задании:
    task_vars = [var for var in dir(task_6_2) if not var.startswith("_")]

    correct_result = "GUIdO vAn ROssUm bEgAn wOrkIng On PYthOn In thE lAtE 1980s"

    assert (
        "result" in task_vars
    ), "Итоговая строка должна быть записана в переменную result"
    assert (
        type(task_6_2.result) == str
    ), f"По заданию в переменной result должна быть строка, а в ней {type(task_6_2.result).__name__}"
    assert (
        correct_result == task_6_2.result
    ), f"В переменной result должна быть строка '{correct_result}'"

