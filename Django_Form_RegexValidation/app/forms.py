from django import forms 
from django.core import validators

class CredForm(forms.Form):
    name=forms.CharField( max_length=54, required=False)
    pno=forms.CharField( max_length=54, required=False,validators=[validators.RegexValidator(r'\+91 ?[6-9]\d{9}')])
    username=forms.CharField( max_length=54, required=False)
    password=forms.CharField( max_length=54, required=False)
    email=forms.EmailField(max_length=254, required=False,validators=[validators.RegexValidator(r'[a-z A-Z]+\.?\w*\@[A-z a-z]+\.[a-z A-Z]{2,3}')])
    profile=forms.ImageField(required=False)
    
    







