from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Ingredient, Recipe, IngredientAmount
from django.forms import inlineformset_factory
from .forms import IngredientForm, RecipeForm

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe/home.html'
    context_object_name = 'recipes'
    ordering = ['-date_posted']


class UserRecipeListView(ListView):
    model = Recipe
    template_name = 'recipe/user_recipes.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Recipe.objects.filter(author=user).order_by('-date_posted')


@login_required
def recipeDetail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    related_ingredients = IngredientAmount.objects.filter(
        recipe__slug=slug)

    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe, 'related_ingredients': related_ingredients})


@login_required
def recipeEdit(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    recipe_edit_form = RecipeForm(request.POST or None, instance=recipe)
    if recipe_edit_form.is_valid():
        recipe_edit_form.save()
        return redirect(reverse("recipe:recipe_detail", kwargs={'slug': str(slug)}))
    return render(request, 'recipe/recipe_edit.html', {'recipe_edit_form': recipe_edit_form})


# @login_required
# def ingredientEdit(request, slug):


# @login_required
# def IngredientAmountEdit(request, slug):


@login_required
def recipeDelete(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == 'POST':
        recipe.delete()
        return redirect('/')
    return render(request, 'recipe/recipe_delete.html', {'recipe': recipe})


@login_required
def recipeBuilder(request):
    recipe_list = Recipe.objects.all()
    recipe = Recipe.objects.filter()
    return render(request, 'recipe/recipe_builder.html', {'title': 'recipe builder', 'recipe_list': recipe_list, 'recipe': recipe})


@login_required
def addIngredient(request):
    ingredient_form = IngredientForm(request.POST)
    ingredient_list = Ingredient.objects.all()

    if request.method == 'POST':
        ingredient_form = IngredientForm(request.POST)
        if ingredient_form.is_valid():
            ingredient_form.save()
            return redirect('recipe:add_ingredient')

    return render(request, 'recipe/add_ingredient.html', {'ingredient_form': ingredient_form, 'ingredient_list': ingredient_list})


@login_required
def addRecipe(request):
    recipe_form = RecipeForm(request.POST)
    recipe_list = Recipe.objects.all()

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect('recipe:add_recipe')

    return render(request, 'recipe/add_recipe.html', {'recipe_form': recipe_form, 'recipe_list': recipe_list})


@login_required
def addIngredientAmount(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    IngredientAmountFormset = inlineformset_factory(
        Recipe, IngredientAmount, fields=('__all__'))

    if request.method == 'POST':
        formset = IngredientAmountFormset(request.POST, instance=recipe)
        if formset.is_valid():
            formset.save()

            return redirect('recipe:add_ingredient_amount', recipe_id=recipe.id)

    formset = IngredientAmountFormset(instance=recipe)

    return render(request, 'recipe/add_ingredient_amount.html', {'formset': formset, 'recipe': recipe})
