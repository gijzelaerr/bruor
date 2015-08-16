from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.TextField()
    public = models.BooleanField(default=True)
    owner = models.ForeignKey(User)
    notes = models.TextField()


class Hop(models.Model):
    name = models.TextField(unique=True)
    country = models.TextField()
    dealer = models.TextField()
    kind = models.TextField()
    alpha_min = models.FloatField()
    alpha_max = models.FloatField()
    beta_min = models.FloatField()
    beta_max = models.FloatField()
    cohumulone_min = models.FloatField()
    cohumulone_max = models.FloatField()
    hopoil_min = models.FloatField()
    hopoil_max = models.FloatField()
    humulene_min = models.FloatField()
    humulene_max = models.FloatField()
    caryophyllene_min = models.FloatField()
    caryophyllene_max = models.FloatField()
    myrcene_min = models.FloatField()
    myrcene_max = models.FloatField()
    farnesene_min = models.FloatField()
    farnesene_max = models.FloatField()
    stability = models.TextField()
    decay = models.FloatField()
    taste = models.TextField()

    def __str__(self):
        return self.name


class Malt(models.Model):
    name = models.TextField(unique=True)
    country = models.TextField(blank=True)
    dealer = models.TextField(blank=True)
    kind = models.TextField()
    color = models.IntegerField()  # EBC
    gravity = models.IntegerField()  # potential gravity gr/l
    max_yield = models.IntegerField()  # maximum yield in % FG
    max_dump = models.IntegerField()   # in %
    moisture = models.IntegerField()  # in %
    protein = models.IntegerField()   # protein level in %
    maisch = models.BooleanField()   # Should be used during maisch

    def __str__(self):
        return self.name


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
