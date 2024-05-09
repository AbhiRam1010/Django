from django import forms
from app.models import *


class Topicform(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'

        
        
class Websiteform(forms.ModelForm):
    class Meta:
        model= Website
        fields= '__all__'


class Accessform(forms.ModelForm):
    class Meta:
        model= Access
        fields= '__all__'
        