from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from .forms import authform

urlpatterns=[
    path('', views.index, name='homepg'),
    path('loginpg', include('django.contrib.auth.urls')),
    path('regpg', views.registrationpage, name='regpg'),
    path('loginpg',auth_views.LoginView.as_view(template_name = "hosp/loginpage.html", authentication_form = authform), name = "LF"),
]