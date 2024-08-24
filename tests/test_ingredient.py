from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from stuff.test_data import Data


class TestIngredient:
    def test_get_price_returns_price(self):
        fresh_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SAUCE_1_NAME, Data.SAUCE_1_PRICE)
        assert fresh_ingredient.get_price() == Data.SAUCE_1_PRICE

    def test_get_name_returns_name(self):
        fresh_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SAUCE_1_NAME, Data.SAUCE_1_PRICE)
        assert fresh_ingredient.get_name() == Data.SAUCE_1_NAME

    def test_get_type_returns_type(self):
        fresh_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SAUCE_1_NAME, Data.SAUCE_1_PRICE)
        assert fresh_ingredient.get_type() == INGREDIENT_TYPE_SAUCE
