from django.db import models


# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=50)

class Animal(models.Model):
    legs= models.IntegerField()
    weight = models.FloatField()
    speed = models.IntegerField()
    heigh= models.FloatField()
    family= models.ForeignKey(Family,on_delete=models.CASCADE)
    def __repr__(self):
        return f"Q{self.id}: {self.text}"
