import pytest

from src.decorators import log


def test_log_file():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    with open('mylog.txt') as f:
        line = f.readline()
        assert line == "my_function ok\n"


def test_log(capsys):
    @log(filename=None)
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    result = capsys.readouterr()
    assert result.out == "my_function ok\n"


def test_log_str(capsys):
    @log(filename=None)
    def my_function(x, y):
        return x + y

    my_function(1, "2")
    result = capsys.readouterr()
    assert result.out == "my_function error: TypeError. Inputs: (1, '2'), {}\n"
