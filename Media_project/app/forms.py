from app.models import *
from django import forms


class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields =['first_name','last_name','email','username','password']
        widgets={'password':forms.PasswordInput}
        help_texts={'password':''}
    
class Profileform(forms.Form):
    class Meta:
        model =Profile
        exclude= ['username']
        