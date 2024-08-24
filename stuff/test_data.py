from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Data:
    BUN_NAME = 'Bread'
    BUN_PRICE = 10.10
    SAUCE_1_NAME = 'First sauce'
    SAUCE_1_PRICE = 11.11
    SAUCE_2_NAME = 'Second sauce'
    SAUCE_2_PRICE = 12.12
    FILLING_1_NAME = 'First filling'
    FILLING_1_PRICE = 13.13
    FILLING_2_NAME = 'Second filling'
    FILLING_2_PRICE = 14.14
    OPTION_1_FULL_PRICE = (BUN_PRICE * 2) + SAUCE_1_PRICE + FILLING_1_PRICE
    OPTION_1_EXPECTED_RECEIPT = (
        f"(==== {BUN_NAME} ====)\n"
        f"= {SAUCE_1_NAME} =\n"
        f"= {FILLING_1_NAME} =\n"
        f"(==== {BUN_NAME} ====)\n\n"
        f"Price: {OPTION_1_FULL_PRICE}"
    )
