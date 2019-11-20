from peewee import *


DATABASE = SqliteDatabase('recipes.sqlite')


class Recipe(Model):
    name = CharField()
    ingredients = CharField()
    directions = TextField()
    nutrients = CharField()
    servings = CharField()
    user_id = CharField()

    class Meta: database = DATABASE



def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Recipe], safe=True)
    print("TABLES Created")
    DATABASE.close()