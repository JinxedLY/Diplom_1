import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun_mock():
    bun_mock = Mock()
    bun_mock.get_price.return_value = 20.20
    bun_mock.get_name.return_value = "bun_mock"
    return bun_mock


@pytest.fixture
def sauce_mock():
    sauce_mock = Mock()
    sauce_mock.get_price.return_value = 25.25
    sauce_mock.get_name.return_value = "sauce_mock"
    sauce_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE


@pytest.fixture
def filling_mock():
    filling_mock = Mock()
    filling_mock.get_price.return_value = 35
    filling_mock.get_name.return_value = "filling_mock"
    filling_mock.get_type.return_value = INGREDIENT_TYPE_FILLING
