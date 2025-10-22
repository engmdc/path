from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-lg ps-5',
            'placeholder': 'Email address or username',
            'id': 'email',
            'autofocus': True,
            'autocomplete': 'username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-lg ps-5',
            'placeholder': 'Password',
            'id': 'password',
            'autocomplete': 'current-password'
        }
    ))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-input',
            'id': 'remember'
        }
    ))

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-lg ps-5',
            'placeholder': 'First Name',
            'id': 'firstname',
            'required': True,
            'autocomplete': 'given-name'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-lg ps-5',
            'placeholder': 'Last Name',
            'id': 'lastname',
            'required': True,
            'autocomplete': 'family-name'
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-lg ps-5',
            'placeholder': 'Username',
            'required': True,
            'autocomplete': 'username'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control form-control-lg ps-5',
            'placeholder': 'Email address',
            'id': 'email',
            'required': True,
            'autocomplete': 'email'
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-lg ps-5',
            'placeholder': 'Password',
            'id': 'password',
            'required': True,
            'autocomplete': 'new-password'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-lg ps-5',
            'placeholder': 'Confirm Password',
            'id': 'confirm_password',
            'required': True,
            'autocomplete': 'new-password'
        }
    ))
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
