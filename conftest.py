import pytest
from unittest.mock import Mock
from stuff.test_data import Data
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun_mock():
    bun_mock = Mock()
    bun_mock.get_price.return_value = Data.BUN_PRICE
    bun_mock.get_name.return_value = Data.BUN_NAME
    return bun_mock


@pytest.fixture
def sauce_mock():
    sauce_mock = Mock()
    sauce_mock.get_price.return_value = Data.SAUCE_1_PRICE
    sauce_mock.get_name.return_value = Data.SAUCE_1_NAME
    sauce_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE


@pytest.fixture
def filling_mock():
    filling_mock = Mock()
    filling_mock.get_price.return_value = Data.FILLING_1_PRICE
    filling_mock.get_name.return_value = Data.FILLING_1_NAME
    filling_mock.get_type.return_value = INGREDIENT_TYPE_FILLING
