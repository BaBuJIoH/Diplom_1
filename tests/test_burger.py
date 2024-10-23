from ingredient import Ingredient
from bun import Bun
from burger import Burger
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:

    def test_burger_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_burger_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_burger_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1

    def test_burger_get_price(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 300  # Булка * 2 + ингредиент
        