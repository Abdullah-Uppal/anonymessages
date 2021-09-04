from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from .models import *
from django.contrib.auth.forms import forms
from django.forms import ModelForm

class URLCreationForm(ModelForm):
  class Meta: 
    model = URL
    fields = ['url', 'name',]