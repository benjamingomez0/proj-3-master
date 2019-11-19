* 3- Ingredient Recipe App

We're developing an app where users will can share and find 3-ingredient recipes.

Users and guest can browse simple 3-ingredient user-generated recipes. 

Users can create recipes using up to 3 main ingredients and as much spice and seasoning as needed.  The app will display the ingredients, instructions to prepare the recipe, serving sizes, and nutritional value.

* Data
The data will be organized in 3 models. Users, Recipes, and Ingredients

Users MVP:
userId
email - unique
name    {
            first,
            last,
            display = first name + last initial
        }
*recipes will be linked to users by userId

Users Stretch:
profilePic (or default avatar)
bio
dietaryRestrictions
allergies
interest

Recipes MVP:
name
userId
ingredients {
            ingredientName
            ingredientId
            quantity
            nutritionalData {
                    calories
                }
            }
servingSize
tags []
    - category, class, region, etc

Recipes Stretch:
time    {
            active
            total
        }
pictures
comments
ratings
allergyInfo

Ingredients MVP:
ID
nutritionalValue

Ingredients Stretch:
allergyInfo
category

* Technology

We'll be using React for the front end, to create a dynamic single page app. Flask will be used to manage the data on the backend. And we'll be using external APIs for nutritional value.