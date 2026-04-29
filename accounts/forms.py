from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import re


class SecureLoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Usuario',
            'autocomplete': 'username'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'autocomplete': 'current-password'
        })
    )


User = get_user_model()

class SecureSignupForm(UserCreationForm):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@empresa.com'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario'
            }),
            'role': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo ya está registrado.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        if len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")

        if not re.search(r"[A-Z]", password):
            raise ValidationError("Debe contener al menos una letra mayúscula.")

        if not re.search(r"[0-9]", password):
            raise ValidationError("Debe contener al menos un número.")

        return password
