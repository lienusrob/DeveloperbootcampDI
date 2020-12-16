from  .  import views 
from django.urls import path, include
from .views import list_family_animals, show_animal_info, list_animals 
# urlpatterns = [
#     path('Familiy/<int:id>' , views.info  ),


# ]

urlpatterns = [
    path('family/<int:id>' ,list_family_animals),
    path('animal/<int:id>' ,show_animal_info),
    path('animals' ,list_animals),
]



#   path('' , views.giphy_app, name= "gify_app")