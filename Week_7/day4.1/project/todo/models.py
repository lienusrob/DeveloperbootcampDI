from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    details = models.CharField(max_length=50)
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateField(auto_now=True)
    date_completion = models.DateField()

#         Create a Todo Model with the fields :
# title
# details
# has_been_done : set by default to false
# date_creation (when the user created the todo)
# date_completion (when the user finished the todo)
# deadline_date (when the user has to finish the todo)


class Category(models.Model):
    name = models.CharField(max_length=50)
    
# Create a Category Model with the fields :
# name
# image (for now a URL field)
# This model has a Many to Many relationship with the Todo Model : A Todo can have many categories, and a category can be shared among many todos.
# Example of category : work, home, shopping, studies, social