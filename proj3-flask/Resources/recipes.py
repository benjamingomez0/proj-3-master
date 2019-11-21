import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

recipe = Blueprint('recipes','recipe')

#Create Route for Recipes
@recipe.route('/', methods=["POST"])
def create_recipe():
   payload = request.get_json()
   recipe = models.Recipe.create(**payload)
   recipe_dict = model_to_dict(recipe)
   print(payload)
   print(recipe_dict)
   return jsonify(data=recipe_dict, status={"code": 201, "message": "Success"})
   


