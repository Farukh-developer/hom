from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput({"class":"form-control" }))
    password = forms.CharField(widget=forms.TextInput({"class":"form-control", "type":"password"}))


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput({"class":"form-control" }))
    first_name = forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput({"class":"form-control" }))
    email = forms.CharField(widget=forms.TextInput({"class":"form-control", "type":"email"}))
    password = forms.CharField(widget=forms.TextInput({"class":"form-control", "type":"password"}))
    confirm_password = forms.CharField(widget=forms.TextInput({"class":"form-control", "type":"password"}))
    

    
    