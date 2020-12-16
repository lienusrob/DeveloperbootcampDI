from django.db import models
from datetime import datetime

# Create your models here.
# how would my modle look for this particlar task where i dont have to
#form


class Country(models.Model):
    name= models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Category(models.Model):
    name= models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Director(models.Model): 
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    def __str__(self):
        return self.first_name

class Film(models.Model):
    title= models.CharField(max_length=50)
    release_date = models.DateField(default=datetime.now)
    created_in_country = models.ForeignKey(Country, null= True, on_delete= models.CASCADE, related_name= '%(class)s_country_creator')
    available_in_countries = models.ManyToManyField(Country,  related_name= '%(class)s_aviaible_country')
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)

    def __str__(self):
        return self.title

