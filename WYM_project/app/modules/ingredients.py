# backend/modules/ingredients.py
from flask import Blueprint

ingredients = Blueprint("ingredients", __name__)

@ingredients.route("/")
def get_ingredients():
    return "Hello world from ingredients"