from django import forms
from django.forms import ModelForm
from .models import Account

# Client Register Form 

class ClientForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['full_name', 'company_name', 'email', 'password']

    def __init__(self, *args, **kwargs):
            super(ClientForm, self).__init__(*args, **kwargs)
            self.fields['email'].widget.attrs['placeholder']='Enter the Email'
            self.fields['password'].widget.attrs['placeholder']='Enter the Email'
            self.fields['company_name'].widget.attrs['placeholder']='Enter First Name'
            self.fields['full_name'].widget.attrs['placeholder']='Enter Last Name'
            
            
            for field in self.fields:
                self.fields[field].widget.attrs['class']='form-control'
# Developer Register Form

class DevForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['full_name', 'company_name', 'email', 'password']

    def __init__(self, *args, **kwargs):
            super(DevForm, self).__init__(*args, **kwargs)
            self.fields['email'].widget.attrs['placeholder']='Enter the Email'
            self.fields['password'].widget.attrs['placeholder']='Enter the Email'
            self.fields['full_name'].widget.attrs['placeholder']='Enter First Name'
            self.fields['company_name'].widget.attrs['placeholder']='Enter Last Name'
            
            
            for field in self.fields:
                self.fields[field].widget.attrs['class']='form-control'