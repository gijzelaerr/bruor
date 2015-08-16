from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.TextField()
    public = models.BooleanField(default=True)
    owner = models.ForeignKey(User)


class Hop(models.Model):
    name = models.TextField()


class Malt(models.Model):
    name = models.TextField()


class OtherIngredient(models.Model):
    name = models.TextField()


class HopInRecipe(models.Model):
    name = models.TextField()
    recipe = models.ForeignKey(Recipe)
    alpha = models.FloatField()
    weight = models.FloatField()  # in grams
    base_hop = models.ForeignKey(Hop)


class MaltInRecipe(models.Model):
    name = models.TextField()
    recipe = models.ForeignKey(Recipe)

    weight = models.FloatField()  # in grams
    base_malt = models.ForeignKey(Malt)


class OtherIngredientInRecipe(models.Model):
    name = models.TextField()
