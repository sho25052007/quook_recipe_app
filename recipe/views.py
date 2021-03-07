from django.shortcuts import render, redirect
from .models import Ingredient, Recipe, IngredientAmount
from django.forms import inlineformset_factory
from .forms import IngredientForm, RecipeForm


def home(request):
    recipe_list = Recipe.objects.all()
    recipe = Recipe.objects.filter()
    return render(request, 'recipe/home.html', {'title': 'home', 'recipe_list': recipe_list, 'recipe': recipe})


def addIngredient(request):
    ingredient_form = IngredientForm(request.POST)
    ingredient_list = Ingredient.objects.all()

    if request.method == 'POST':
        ingredient_form = IngredientForm(request.POST)
        if ingredient_form.is_valid():
            ingredient_form.save()
            return redirect('add_ingredient')

    return render(request, 'recipe/add_ingredient.html', {'ingredient_form': ingredient_form, 'ingredient_list': ingredient_list})


def addRecipe(request):
    recipe_form = RecipeForm(request.POST)
    recipe_list = Recipe.objects.all()

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect('add_recipe')

    return render(request, 'recipe/add_recipe.html', {'recipe_form': recipe_form, 'recipe_list': recipe_list})


def addIngredientAmount(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    recipes = recipe.ingredient_amounts.all()
    # recipe_selected = Recipe.objects.filter(id=recipe_id)
    IngredientAmountFormset = inlineformset_factory(
        Recipe, IngredientAmount, fields=('__all__'))

    if request.method == 'POST':
        formset = IngredientAmountFormset(request.POST, instance=recipe)
        if formset.is_valid():
            formset.save()

            return redirect('add_ingredient_amount', recipe_id=recipe.id)

    formset = IngredientAmountFormset(instance=recipe)

    return render(request, 'recipe/add_ingredient_amount.html', {'formset': formset, 'recipe': recipe, 'recipes': recipes})