# Generated by Django 3.1.7 on 2021-03-07 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='name',
            new_name='title',
        ),
    ]
