from django import forms
from .models import package
from django.contrib.auth.forms import UserCreationForm#Sfrom django.contrib.auth.models import User

class packageform(forms.ModelForm):
    class Meta:
        model = package
        fields = ('name','phone_number','address','service','track_id')
