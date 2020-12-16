from  .  import views 
from django.urls import path

urlpatterns = [
    path('' , views.home, name= "gif"),
    path('add', views.add, name="add")
]
