import pytest
from tools.is_palindrome_number import run


def test_is_palindrome_number_basic():
    assert run("121") == "True"
    assert run("12321") == "True"
    assert run("7") == "True"
    assert run("123") == "False"
    assert run("10") == "False"


def test_is_palindrome_number_negative():
    assert run("-121") == "False"


def test_is_palindrome_number_errors():
    assert run() == "Error: Please provide exactly one argument."
    assert run("121", "121") == "Error: Please provide exactly one argument."
    assert run("") == "Error: Argument cannot be empty."
    assert run("   ") == "Error: Argument cannot be empty."
    assert run("abc") == "Error: Argument must be an integer."
    assert run("12.21") == "Error: Argument must be an integer."
