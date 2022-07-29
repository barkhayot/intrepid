from django.urls import path
from . import views

urlpatterns = [
    path('cli-register', views.Client_Register, name='cli-register'),
    path('dev-register', views.Dev_Register, name='dev-register'),
    path('login', views.Login_View, name='login'),
    path('logout', views.Logout_View, name='logout')
]