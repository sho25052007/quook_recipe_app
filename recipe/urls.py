from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe_builder', views.recipeBuilder, name='recipe_builder'),
    path('add/ingredient/', views.addIngredient, name='add_ingredient'),
    path('add/recipe/', views.addRecipe, name='add_recipe'),
    path('add/ingredient_amount/<str:recipe_id>/',
         views.addIngredientAmount, name='add_ingredient_amount'),

]
