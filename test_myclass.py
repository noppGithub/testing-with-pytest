import pytest
from myclass import MyClass, MyClassError


def test_add():
    calculator = MyClass()
    result = calculator.add(2, 3)
    assert result == 5


def test_add_weird_stuff():
    calculator = MyClass()
    with pytest.raises(MyClassError):
        result = calculator.add("two", 3)


def test_add_weirder_stuff():
    calculator = MyClass()
    with pytest.raises(MyClassError):
        result = calculator.add("two", "three")


def test_subtract():
    calculator = MyClass()
    result = calculator.subtract(9, 3)
    assert result == 6


def test_multiply():
    calculator = MyClass()
    result = calculator.multiply(9, 3)
    assert result == 27


def test_divide():
    calculator = MyClass()
    result = calculator.divide(9, 3)
    assert result == 3


def test_divide_by_zero():
    calculator = MyClass()
    with pytest.raises(MyClassError):
        result = calculator.divide(9, 0)
