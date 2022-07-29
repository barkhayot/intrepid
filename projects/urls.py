from django.urls import path
from . import views

urlpatterns = [
    path('get', views.GetProjects, name='getprojects'),
    path('get/<int:pk>', views.GetProjectDetail, name='detail'),
    path('create', views.CreateProject, name='create'),
    path('delete/<int:pk>', views.DeleteProject, name='delete')
]