from .models import Project
from django import forms
from django.forms import ModelForm

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'desc', 'deadline', 'status']