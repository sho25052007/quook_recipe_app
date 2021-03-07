from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/ingredient/', views.addIngredient, name='add_ingredient'),
    path('add/recipe/', views.addRecipe, name='add_recipe'),
    path('add/ingredient_amount/<str:recipe_id>/',
         views.addIngredientAmount, name='add_ingredient_amount'),

]
