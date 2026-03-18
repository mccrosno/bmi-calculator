import pytest
from bmi import get_bmi


def test_valid_inputs():
    assert get_bmi(150, 65) == pytest.approx(24.96, abs=0.01)


def test_valid_low_weight():
    assert get_bmi(1, 65) == pytest.approx(0.17, abs=0.01)


def test_valid_high_weight():
    assert get_bmi(300, 65) == pytest.approx(49.92, abs=0.01)


def test_valid_low_height():
    assert get_bmi(150, 24) == pytest.approx(183.10, abs=0.01)


def test_valid_high_height():
    assert get_bmi(150, 108) == pytest.approx(9.04, abs=0.01)


def test_zero_weight():
    with pytest.raises(ValueError):
        get_bmi(0, 65)


def test_negative_weight():
    with pytest.raises(ValueError):
        get_bmi(-150, 65)


def test_zero_height():
    with pytest.raises(ValueError):
        get_bmi(150, 0)


def test_negative_height():
    with pytest.raises(ValueError):
        get_bmi(150, -65)


def test_both_zero():
    with pytest.raises(ValueError):
        get_bmi(0, 0)
