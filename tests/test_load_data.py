import pytest
from autotest_data.load_data import load_data


@pytest.mark.parametrize("test_input,expected", [
    (2, 4),
    (-2, -4),
    (100, 200)
])
def test_data(test_input, expected):
    assert load_data(test_input) is expected


@pytest.mark.skip(reason="input checking not implemented")
def test_invalid_data_input():
    with pytest.raises(ValueError):
        load_data("2")


@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1


def test_print(capture_stdout):
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"
