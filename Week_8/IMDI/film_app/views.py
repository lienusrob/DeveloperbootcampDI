from django.http.request import RawPostDataException
from django.shortcuts import render
from .forms import addDirectorForm, addFilmForm
from .models import *

# Create your views here.


def home(request):
    return render (request, "homepage.html")


def addDirector(request):
    if request.method== "POST":
        form = addDirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return render('homepage.html')

        
    else:
        form = addDirectorForm(request.POST)
        return render (request, "addDirector.html", {'form':form} )

def addFilm(request):
    return render (request, "addFilm.html" )