from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    ingredients = models.ManyToManyField(
        'Ingredient', through='IngredientAmount', related_name='recipes')

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class IngredientAmount(models.Model):
    SINGLE = 1
    DOUBLE = 2
    TRIPLE = 3
    AMOUNT_CHOICES = (
        (SINGLE, 'Single'),
        (DOUBLE, 'Double'),
        (TRIPLE, 'Triple'),
    )

    recipe = models.ForeignKey(
        'Recipe', related_name='ingredient_amounts', on_delete=models.SET_NULL, null=True)
    ingredient = models.ForeignKey(
        'Ingredient', related_name='ingredient_amounts', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.IntegerField(choices=AMOUNT_CHOICES, default=SINGLE)
