import pytest
from tools.longest_common_prefix import run


def test_longest_common_prefix_basic():
    assert run("flower,flow,flight") == "fl"
    assert run("flower,flow") == "flow"
    assert run("dog,racecar,car") == ""
    assert run("interspecies,interstellar,interstate") == "inters"
    assert run("throne,throne") == "throne"


def test_longest_common_prefix_errors():
    assert run() == "Error: Please provide exactly one argument."
    assert run("flower,flow", "flight") == "Error: Please provide exactly one argument."
    assert run("single") == "Error: Please provide a comma-separated list of at least two strings (e.g. 'flower,flow,flight')."
