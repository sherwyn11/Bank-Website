from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    contact = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zip = forms.CharField()
    password = forms.CharField()
    
