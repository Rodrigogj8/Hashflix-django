from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class FormHomepage(forms.Form):
    email = forms.EmailField(required=True)


class CriarContaForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']