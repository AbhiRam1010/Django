from django import forms
from app.models import *
import re

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','password','email','username']
        help_texts={'username':''}
        widgets={'password':forms.PasswordInput}

        
class ProfileForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        exclude=['username']


    def pno_cleaner(self):
            pno = self.cleaned_data['pno']
            if re.match(r"(?:\+91 ?)? [6-9]\d{9}",pno):
                return pno
            return None
        