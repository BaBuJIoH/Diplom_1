from database import Database
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE
from unittest.mock import patch

class TestDatabase:

    @patch('database.Database.available_buns')
    def test_database_available_buns(self, mock_available_buns):
        mock_available_buns.return_value = [Bun("black bun", 100)]
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 1
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100

    @patch('database.Database.available_ingredients')
    def test_database_available_ingredients(self, mock_available_ingredients):
        mock_available_ingredients.return_value = [Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)]
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 1
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_price() == 100
