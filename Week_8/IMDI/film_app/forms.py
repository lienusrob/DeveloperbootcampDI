from django.forms import ModelForm
from django import forms
from .models import Country, Director, Category, Film


class addFilmForm(ModelForm):

    class Meta:
        model = Film 
        fields = '__all__'


class addDirectorForm(ModelForm):

    class Meta:
        model = Director 
        fields = '__all__'


   
