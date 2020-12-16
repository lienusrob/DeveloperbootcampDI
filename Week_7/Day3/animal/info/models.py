from django.db import models



class aninmal(models.Model):
    legs= models.IntegerField(max_length=30)
    weight = models.IntegerField()
    speed = models.IntegerField()
    heigh= models.IntegerField()
    family= models.IntegerField()
    def __repr__(self):
        return f"Q{self.id}: {self.text}"
# Create your models here.
class animalfam(models.Model):
    family= models.CharField(max_length=30)
    def __repr__(self):
        return f"Q{self.id}: {self.text}"