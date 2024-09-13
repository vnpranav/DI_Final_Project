from django.contrib.auth.forms import UserCreationForm
from django import forms 
from .models import User

class CustomUserForm(UserCreationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control my-2', 'placeholder' : 'Enter username'}))
   email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control my-2', 'placeholder' : 'Enter email'}))
   password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control my-2', 'placeholder' : 'Enter password'}))
   password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control my-2', 'placeholder' : 'Enter Confirm password'}))
   class Meta:
      model = User
      fields = ['username', 'email', 'password1', 'password2']