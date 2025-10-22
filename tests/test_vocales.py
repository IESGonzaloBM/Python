import pytest

from src.vocales import saca_vocales

@pytest.mark.parametrize(
    "input_x, expected",
    [
        ("JRK", ""),
        ("HolA", "oa"),
        ("quetal", "uea")
    ]
)

def test_saca_vocales(input_x, expected):
    assert saca_vocales(input_x) == expected
