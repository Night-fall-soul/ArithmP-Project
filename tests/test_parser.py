import pytest

from arithmp.parser import Parser


def test_multiplication():
    parser = Parser()
    assert parser.parse("3 * 4") == 12.0


def test_addition():
    parser = Parser()
    assert parser.parse("2 + 3") == 5.0


def test_subtraction():
    parser = Parser()
    assert parser.parse("10 - 4") == 6.0


def test_division():
    parser = Parser()
    assert parser.parse("8 / 2") == 4.0


def test_operator_precedence():
    parser = Parser()
    assert parser.parse("2 + 3 * 4") == 14.0


def test_division_by_zero():
    parser = Parser()
    with pytest.raises(ZeroDivisionError):
        parser.parse("5 / 0")
