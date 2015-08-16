# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HopInRecipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('alpha', models.FloatField()),
                ('weight', models.FloatField()),
                ('base_hop', models.ForeignKey(to='recipe.Hop')),
            ],
        ),
        migrations.CreateModel(
            name='Malt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MaltInRecipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('weight', models.FloatField()),
                ('base_malt', models.ForeignKey(to='recipe.Malt')),
            ],
        ),
        migrations.CreateModel(
            name='OtherIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OtherIngredientInRecipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('public', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='maltinrecipe',
            name='recipe',
            field=models.ForeignKey(to='recipe.Recipe'),
        ),
        migrations.AddField(
            model_name='hopinrecipe',
            name='recipe',
            field=models.ForeignKey(to='recipe.Recipe'),
        ),
    ]
