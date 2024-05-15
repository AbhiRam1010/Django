from django import forms 
from app.models import *
import re

class CredForm (forms.ModelForm):
    class Meta:
        model= Credential
        fields='__all__'

        
    def clean_pno(self):
        pno = self.cleaned_data.get('pno')
        if re.match(r'(?:\+91 ?)?[6-9]\d{9}',pno):
            return pno
        return None
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if re.match(r'[A-Z a-z]+\.?\w+\@[A-Z a-z]+\.[A-Z a-z]{2,3}', email):
            return email
        return None

