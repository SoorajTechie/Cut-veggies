from django import forms
from .models import customer



class CustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ['name','quantity','cust','address','phone']

        