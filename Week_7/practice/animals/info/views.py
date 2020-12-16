from django.shortcuts import render
from django.http import HttpResponse 
from django.http.response import HttpResponse

# Create your views here.

def list_family_animals(request, id):
    return render(request, 'list_family_animals.html')

def show_animal_info(request, id):
    return render(request, 'show_animal_info.html')

def list_animals(request):
    return render(request, 'list_animals.html')

