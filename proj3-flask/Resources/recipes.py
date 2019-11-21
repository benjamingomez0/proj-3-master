import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

recipe = Blueprint('recipes','recipe')

#Show Route for individual Recipes
@recipe.route('/<id>', methods=["GET"])
def get_recipe(id):
    try:
    recipe = model_to_dict(models.Recipe.get_by_id(id))
    return jsonify(data=recipe, status={"code":201, "message":"Succes"})
    except models.DoesNotExist:
    return jsonify(data={}, status={"code": 401, "message": "Error"  })

#Create Route for Recipes
@recipe.route('/', methods=["POST"])
def create_recipe():
   payload = request.get_json()
   recipe = models.Recipe.create(**payload)
   recipe_dict = model_to_dict(recipe)
   return jsonify(data=recipe_dict, status={"code": 201, "message": "Success"})
   


