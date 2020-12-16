from django.db import models
from django.shortcuts import render
from .models import Profile
from django.views.generic import ListView, DetailView
# Create your views here.

class UserListView(ListView):
    model = Profile 


class UserDetailView (DetailView): 
    modle= Profile 
    

