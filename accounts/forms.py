from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
    class Meta: #something to define the class
        model = Order
        fields = '__all__'
        # fields = ['cusomter', 'product'] # if u just need some field
