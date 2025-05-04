from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#clase que contiene el formulario para crear usuario usando modelo de django
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingresa un email válido.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')