from django.db import models

# Create your models here.

class gif(models.Model):
    title= models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    uploader_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class category(models.Model):
    name= models.CharField(max_length=50)
    gifs = models.ManyToManyField(gif)

    def __str__(self):
        return self.name



