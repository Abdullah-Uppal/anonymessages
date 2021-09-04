from django.shortcuts import render
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.



class SignUpView(CreateView):
    model = get_user_model()
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
