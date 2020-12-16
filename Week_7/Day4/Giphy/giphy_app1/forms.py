from django.forms import ModelForm
from django import forms
from .models import category, gif


class GifForm(ModelForm):
    class Meta:
        model = gif
        fields = ['uploader_name', 'title', 'url']

class CategoriesForm(ModelForm):
    class Meta:
        model = category 
        fields = ['name', 'gifs']

# GifForm
# uploader_name
# title
# url


