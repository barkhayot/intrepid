from django import forms
from django.forms import ModelForm
from .models import Account

# Client Register Form 

class ClientForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['full_name', 'company_name', 'email', 'password']

# Developer Register Form

class DevForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['full_name', 'company_name', 'email', 'password']