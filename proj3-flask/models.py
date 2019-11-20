from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('recipes.sqlite')


class Recipe(Model):
    name = CharField()
    ingredients = CharField()
    directions = TextField()
    nutrients = CharField()
    servings = CharField()
    user_id = CharField()

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


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Recipe, User], safe=True)
    print("TABLES Created")
    DATABASE.close()