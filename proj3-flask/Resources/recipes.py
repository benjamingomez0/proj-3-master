import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

recipe = Blueprint('recipes','recipe')
#Show Route for all Recipes

@recipe.route('/', methods=["GET"])
def get_all_recipes():
    try:
        recipes = [model_to_dict (recipe) for recipe in models.Recipe.select()]
        return jsonify(data = recipes,status={"code": 201, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})

#Show Route for individual Recipes
@recipe.route('/<id>', methods=["GET"])
def get_recipe(id):
    try:
        recipe = model_to_dict(models.Recipe.get_by_id(id))
        return jsonify(data=recipe, status={"code":201, "message":"Succes"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error Retrieving Information"})