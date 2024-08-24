import pytest
from stuff.test_data import Data
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns_sets_the_bun(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    @pytest.mark.parametrize('ingredient', ['filling_mock', 'sauce_mock'])
    def test_add_ingredient_add_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert ingredient in burger.ingredients

    @pytest.mark.parametrize('ingredient', ['filling_mock', 'sauce_mock'])
    def test_remove_ingredient_removes_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_rearranges_ingredients(self, burger_fixture, filling_mock, sauce_mock):
        burger_fixture.move_ingredient(1, 0)
        assert burger_fixture.ingredients[0] == sauce_mock
        assert burger_fixture.ingredients[1] == filling_mock

    def test_get_price_gets_price(self, burger_fixture):
        assert burger_fixture.get_price() == Data.OPTION_1_FULL_PRICE

    def test_get_receipt_gets_recipe(self, burger_fixture):
        burger_fixture.get_receipt() == Data.OPTION_1_EXPECTED_RECEIPT
