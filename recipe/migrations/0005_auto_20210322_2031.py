# Generated by Django 3.1.7 on 2021-03-22 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='default-recipe.jpg', upload_to='recipe_pics'),
        ),
    ]
