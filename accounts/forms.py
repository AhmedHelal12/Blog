from typing import Any
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

attrs = {"class":"form-control"}

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs=attrs)
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs=attrs)
    )

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(attrs=attrs)
    )
    last_name = forms.CharField(
        label="Last name",
        widget=forms.TextInput(attrs=attrs)
    )
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs=attrs)
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs=attrs)
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs=attrs)
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs=attrs)
    )
    class Meta(UserCreationForm.Meta):
        fields = ['first_name','last_name','username','email','password1','password2']


class ProfileForm(UserChangeForm):
    password = None
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        widgets = {
            'first_name':forms.TextInput(attrs=attrs),
            'last_name':forms.TextInput(attrs=attrs),
            'email':forms.EmailInput(attrs=attrs),
        }

