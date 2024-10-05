from django.urls import path,include
from .views import RegisterView,ProfileView
from .forms import LoginForm
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('login/',LoginView.as_view(authentication_form=LoginForm),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('',include('django.contrib.auth.urls'))
]
