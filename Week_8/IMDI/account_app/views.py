from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.contrib.auth.models import User

# Create your views here.
class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    context = {'from_class':form_class}
    success_url = reverse_lazy('login')   

    def form_valid (self, form_class):
        form_class.save()
        return super().form_valid(form_class)  

class Register(View):

    def get(self, request):
        return render(request, 'registration/register.html')

    def post(self, request):

        form = UserCreationForm(request.POST)
        username= request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if form.is_valid():
            user = User.objects.create(username=username, password=password1 )
            user = form.save()
            # Authentication should always be done before login....
            # In this case, we just created the user successfully, so obviously the authenticate will work.
            user = authenticate(form.cleaned_data['username'], form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                return redirect('home')

        return redirect('register')