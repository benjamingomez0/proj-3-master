from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('recipes.sqlite')


class Recipe(Model):
    name = CharField()
    user_id = CharField()
    ingredientId1 = CharField()
    ingredientId2 = CharField()
    ingredientId3 = CharField()
    directions = TextField()
    calories = CharField()
    servings = CharField()

    class Meta: 
        database = DATABASE

class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField()
    first_name = CharField()
    last_name = CharField()
    username = CharField()

    class Meta: 
        database = DATABASE

class Ingredient(Model):
    name = CharField()
    quantity = CharField()

    class Meta: 
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Recipe, User, Ingredient], safe=True)
    print("TABLES Created")
    DATABASE.close()