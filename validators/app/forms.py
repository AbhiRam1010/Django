from app.models import School
from django import forms
from django.core import validators
def b_validater(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('The school name is starting with b')

def len_validetor(data):
    if len(data)>5:
        raise forms.ValidationError('Has more than 5 character')

# def duplicate_validator(data):
#     if data in School.sname:
#         raise forms.ValidationError('already')

class SchoolForm(forms.Form):
    sname=forms.CharField(max_length=50, required=False,validators=[b_validater,len_validetor])
    sprincipal=forms.CharField( max_length=50, required=False)
    saddress=forms.CharField( max_length=50, required=False)
    