

def test_task_stdout(capsys):
    """
    Проверка работы задания
    """
    import task_4_9a

    out, err = capsys.readouterr()
    correct_stdout = "Guido Rossum working Python the 1980s"
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout == out.strip()
    ), "На стандартный поток вывода выводится неправильная строка"

