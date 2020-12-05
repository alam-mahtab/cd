from django import forms
from .models import *
class UserForm(forms.ModelForm):
    class Meta:
        model = User_Data
        password = forms.CharField(widget=forms.PasswordInput)