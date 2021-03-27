from django.urls import path
from .views import RecipeListView, UserRecipeListView
from . import views

app_name = 'recipe'

urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('user-recipes/<str:username>/',
         UserRecipeListView.as_view(), name='user_recipes'),
    path('recipe/<slug:slug>/',
         views.recipeDetail, name='recipe_detail'),
    path('recipe_builder/', views.recipeBuilder, name='recipe_builder'),
    path('add/ingredient/', views.addIngredient, name='add_ingredient'),
    path('add/recipe/', views.addRecipe, name='add_recipe'),
    path('add/ingredient_amount/<str:recipe_id>/',
         views.addIngredientAmount, name='add_ingredient_amount'),

]
