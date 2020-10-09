from django import forms
from .models import  Order

class EntryForm(forms.ModelForm):  
    class Meta:  
        model = Order  
        fields = ('order_connect_mer', 'orderr_connect_stor',  'order_depart_date', 'order_prepare','order_depart')

