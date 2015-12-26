import pytest

from sources.calculator import Calculator
from sources.main import find_next


def test1():
    original = "hello"
    pattern = "a"

    for i in find_next(original, pattern):
        pytest.fail(msg="Invalid pattern founded")


def test2():
    original = [1, 2, 3, 4]
    pattern = [1]

    with pytest.raises(TypeError):
        next(find_next(original, pattern))


def test3():
    original = "hello"
    pattern = ""

    with pytest.raises(RuntimeError):
        next(find_next(original, pattern))


def test4():
    cal = Calculator(10, 5)
    assert hasattr(cal, "number1")
    assert hasattr(cal, "number2")
    assert hasattr(cal, "add")
    assert hasattr(cal, "mul")
    assert hasattr(cal, "sub")
    assert hasattr(cal, "div")
    assert hasattr(cal, "mod")


def test5():
    with pytest.raises(TypeError):
        cal = Calculator()

    with pytest.raises(TypeError):
        cal = Calculator(1)


def test6():
    cal = Calculator(10, 5)
    assert cal.add() == 15
    assert cal.mul() == 50
    assert cal.sub() == 5
    assert cal.div() == 2
    assert cal.mod() == 0
