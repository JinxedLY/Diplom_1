import pytest
from praktikum.bun import Bun
from stuff.test_data import Data


class TestBuns:
    def test_get_bun_name_success(self):
        fresh_bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert fresh_bun.get_name() == Data.BUN_NAME

    def test_get_bun_price_success(self):
        fresh_price = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert fresh_price.get_price() == Data.BUN_PRICE
