import pytest
from bmi import get_bmi, get_category


def test_valid_inputs():
    assert get_bmi(150, 65) == pytest.approx(24.96, abs=0.01)


def test_valid_low_weight():
    assert get_bmi(0.01, 65) == pytest.approx(0.00, abs=0.01)


def test_valid_high_weight():
    assert get_bmi(1000, 65) == pytest.approx(166.40, abs=0.01)


def test_valid_low_height():
    assert get_bmi(150, 24) == pytest.approx(183.10, abs=0.01)


def test_valid_high_height():
    assert get_bmi(150, 108) == pytest.approx(9.04, abs=0.01)


def test_absolute_minimum():
    assert get_bmi(0.01, 0.01) == pytest.approx(70.32, abs=0.01)


def test_absolute_maximum():
    assert get_bmi(1000, 1000) == pytest.approx(0.70, abs=0.01)


def test_zero_weight():
    with pytest.raises(ValueError):
        get_bmi(0, 65)


def test_negative_weight():
    with pytest.raises(ValueError):
        get_bmi(-150, 65)


def test_weight_above_max():
    with pytest.raises(ValueError):
        get_bmi(1001, 65)


def test_zero_height():
    with pytest.raises(ValueError):
        get_bmi(150, 0)


def test_negative_height():
    with pytest.raises(ValueError):
        get_bmi(150, -65)


def test_height_above_max():
    with pytest.raises(ValueError):
        get_bmi(150, 1001)


def test_both_zero():
    with pytest.raises(ValueError):
        get_bmi(0, 0)


def test_category_underweight():
    assert get_category(18.4) == "Underweight"


def test_category_underweight_low():
    assert get_category(1.0) == "Underweight"


def test_category_normal_lower_boundary():
    assert get_category(18.5) == "Normal"


def test_category_normal():
    assert get_category(21.75) == "Normal"


def test_category_normal_upper_boundary():
    assert get_category(24.9) == "Normal"


def test_category_overweight_lower_boundary():
    assert get_category(25.0) == "Overweight"


def test_category_overweight():
    assert get_category(27.5) == "Overweight"


def test_category_overweight_upper_boundary():
    assert get_category(29.9) == "Overweight"


def test_category_obese_lower_boundary():
    assert get_category(30.0) == "Obese"


def test_category_obese():
    assert get_category(35.0) == "Obese"
