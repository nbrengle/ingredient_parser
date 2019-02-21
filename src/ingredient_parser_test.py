"""Tests for `ingredient_parser.py`"""
import pytest

from ingredient_parser import parse_ingredient


@pytest.mark.parametrize(
    "ingredient_str, ingredient_result",
    [
        ("1 cup sugar", {"quantity": "1", "unit": "c", "ingredient": "sugar"}),
        (
            "4 tsp. Orange Juice",
            {"quantity": "4", "unit": "t", "ingredient": "Orange Juice"},
        ),
        ("5 eggs", {"quantity": "5", "unit": None, "ingredient": "eggs"}),
        ("5 cups of salt", {"quantity": "5", "unit": "c", "ingredient": "salt"}),
        (
            "salt and pepper to taste",
            {"quantity": None, "unit": None, "ingredient": "salt and pepper to taste"},
        ),
        (
            "1 teaspoon vanilla extract",
            {"quantity": "1", "unit": "t", "ingredient": "vanilla extract"},
        ),
        (
            "500 g all-purpose flour",
            {"quantity": "500", "unit": "g", "ingredient": "all-purpose flour"},
        ),
        (
            "3.5 GRAMS xanthum gum",
            {"quantity": "3.5", "unit": "g", "ingredient": "xanthum gum"},
        ),
        (
            "20 cups chopped onions",
            {"quantity": "20", "unit": "c", "ingredient": "chopped onions"},
        ),
        (
            "50 grams grampa's potato slaw",
            {"quantity": "50", "unit": "g", "ingredient": "grampa's potato slaw"},
        ),
    ],
)
def test_ingredient_parser(ingredient_str, ingredient_result):
    """Happy Path Test: examples parse into maps as expected."""
    assert parse_ingredient(ingredient_str) == ingredient_result
