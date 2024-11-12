from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', lambda request: redirect('inicio')),
    path('inicio/', auth_views.LoginView.as_view(template_name='aplicacion1/inicio.html'), name='inicio'),
    path('segundo/', views.segundo, name='segundo'),
]