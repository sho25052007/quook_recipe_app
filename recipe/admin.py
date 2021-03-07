from django.contrib import admin
from .models import Recipe, Ingredient, IngredientAmount

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(IngredientAmount)
