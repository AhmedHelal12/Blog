from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['first_name','last_name','username','email']

class ProfileForm(UserChangeForm):
    password = None
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

