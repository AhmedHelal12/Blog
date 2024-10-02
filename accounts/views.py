from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import RegisterForm,ProfileForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    def get_success_url(self) :
        login(self.request,self.object)
        return reverse_lazy('/')


class ProfileView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'registration/profile.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def get_object(self):
        return self.request.user