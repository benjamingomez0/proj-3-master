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
        return jsonify(data=recipe, status={"code":201, "message":"Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error Retrieving Information"})

#Create Route for Recipes
@recipe.route('/', methods=["POST"])
def create_recipe():
   payload = request.get_json()
   recipe = models.Recipe.create(**payload)
   recipe_dict = model_to_dict(recipe)
   return jsonify(data=recipe_dict, status={"code": 201, "message": "Success"})
   
# update route
@recipe.route('/<id>', methods=["PUT"])
def update_recipe(id):
    payload= request.get_json()
    query = models.Recipe.update(**payload).where(models.Recipe.id == id)
    query.execute()
    return jsonify(data=model_to_dict(models.Recipe.get_by_id(id)), status={"code": 201, "message": "Recipe Updated"})

# delete route
@recipe.route('/<id>', methods=["DELETE"])
def delete_recipe(id):
    query = models.Recipe.delete().where(models.Recipe.id==id)
    query.execute()
    return jsonify(data='successfully deleted', status={"code": 201, "message": "Recipe Deleted"})

