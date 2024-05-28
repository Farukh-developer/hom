from django import forms
from .models import Student
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
    
    

class StudentForm(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    last_name=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    
    

    class Meta:
        model=Student
        fields=('first_name', 'last_name', 'interests', 'email', 'location', 'phone', 'image')              

    