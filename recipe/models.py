from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.core.validators import RegexValidator


class Recipe(models.Model):
    alphanumeric = RegexValidator(
        r'[a-zA-Z][a-zA-Z ]+', 'Only alphabet characters and spaces are allowed.')

    title = models.CharField(max_length=30, null=True,
                             validators=[alphanumeric])
    description = models.TextField(max_length=200, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(
        default='default-recipe.jpg', upload_to='recipe_pics')
    slug = models.SlugField(null=False, unique=True)

    ingredients = models.ManyToManyField(
        'Ingredient', through='IngredientAmount', related_name='recipes')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe:recipe_detail', kwargs={'slug': self.slug})

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


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

    def __str__(self):
        return f'Recipe = {self.recipe}, Ingredient = {self.ingredient}, Amount = {self.amount}'
