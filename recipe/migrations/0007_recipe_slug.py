# Generated by Django 3.1.7 on 2021-03-24 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_auto_20210322_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
