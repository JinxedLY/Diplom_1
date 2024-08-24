from praktikum.database import Database


class TestDatabase:

    def test_available_buns_returns_correct_number_of_buns(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_available_ingredients_returns_correct_number_of_ingredients(self):
        database = Database()
        assert len(database.available_ingredients()) == 6
