from django import forms
g = [['Male','Male'], ['Female', 'Female']]
c = [['python', 'Python'], ['Java', 'Java'], ['Testing', 'Testing'], ['Mern', 'Mern']]

class ModelRegisterForm(forms.Form):
    name = forms.CharField( max_length=50, required=False)
    pno = forms.CharField( max_length=13, required=False)
    email= forms.EmailField(required=False)
    add = forms.CharField( max_length=250, required=False, widget=forms.Textarea(attrs={'cols':20,'rows':5}))
    gender = forms.ChoiceField(choices=g, required=False, widget=forms.RadioSelect)
    cource = forms.MultipleChoiceField(choices=c, widget=forms.CheckboxSelectMultiple)
    username = forms.CharField( max_length=50, required=False)
    password = forms.CharField( max_length=50, required=False,widget=forms.PasswordInput)