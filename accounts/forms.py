from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class OrderForm(ModelForm):
    class Meta: #something to define the class
        model = Order
        fields = '__all__'
        # fields = ['cusomter', 'product'] # if u just need some field


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']