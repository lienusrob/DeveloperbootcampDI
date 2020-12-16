from giphy_app1.models import category, gif
from django import forms
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse 
from .forms import CategoriesForm, GifForm


# Create your views here.

def add (request):
    if request.method== 'POST':
        form = GifForm(request.POST)
        form2= CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
        if form2.is_valid():
            form.save()
        return redirect("gif")
    else: 
        form2 = CategoriesForm(request.POST)
        form = GifForm(request.POST)
        return render(request, "add.html", {'form':form, 'form2': form2}) 

def home(request):
    result = gif.objects.all()
    result1 = category.objects.all()
    return render (request, "gif.html", {'reslut': result, 'reslut1': result1})


