from django.shortcuts import render

# Create your views here.

def list_family_animals(request,id):
    return render(request,"info/list_family_animals.html", {"id":id})
    
def show_animal_info(request,id):
    return render(request,"info/show_animal_info.html", {"id":id})

def list_animals(request):
    return render(request,"info/list_animals.html") 


