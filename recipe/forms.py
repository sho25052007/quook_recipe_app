from django.forms import ModelForm
from .models import Ingredient, Recipe


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name',)


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
