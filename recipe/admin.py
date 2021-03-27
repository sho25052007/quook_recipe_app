from django.contrib import admin
from .models import Recipe, Ingredient, IngredientAmount

admin.site.register(Ingredient)
admin.site.register(IngredientAmount)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date_posted',
                    'author', 'image')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Recipe, RecipeAdmin)
