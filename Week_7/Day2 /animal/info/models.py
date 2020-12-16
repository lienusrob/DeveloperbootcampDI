from django.db import models

# Create your models here.


class animalmod(models.Model):
    familyname = models.IntegerField()
    def __repr__(self):
        return f"Q{self.id}: {self.text}"
    
