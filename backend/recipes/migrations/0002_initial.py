# Generated by Django 3.2 on 2023-12-13 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(help_text='Provide a set of tags it belongs to', through='recipes.RecipeTag', to='recipes.Tag', verbose_name='Set of tags'),
        ),
        migrations.AddField(
            model_name='ingredientamountinrecipe',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes_in', to='recipes.ingredient'),
        ),
        migrations.AddField(
            model_name='ingredientamountinrecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.recipe'),
        ),
        migrations.AddConstraint(
            model_name='ingredient',
            constraint=models.UniqueConstraint(fields=('name', 'measurement_unit'), name='name & measurement_unit must make a unique pair'),
        ),
        migrations.AddField(
            model_name='favoriteitem',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites_in', to='recipes.recipe'),
        ),
        migrations.AddField(
            model_name='favoriteitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts_in', to='recipes.recipe'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='recipetag',
            constraint=models.UniqueConstraint(fields=('recipe', 'tag'), name='recipe & tag must make a unique pair'),
        ),
        migrations.AddConstraint(
            model_name='ingredientamountinrecipe',
            constraint=models.UniqueConstraint(fields=('recipe', 'ingredient'), name='recipe & ingredient must make a unique pair'),
        ),
        migrations.AddConstraint(
            model_name='favoriteitem',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='already in favorites'),
        ),
        migrations.AddConstraint(
            model_name='cartitem',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='already in shopping cart'),
        ),
    ]
