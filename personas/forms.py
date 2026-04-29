from django import forms
from .models import Persona
from django.core.exceptions import ValidationError
from datetime import date
from .models import Nota


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese apellido'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@email.com'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'genero': forms.Select(attrs={
                'class': 'form-select'
            }),
            'direccion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'rol': forms.Select(attrs={
                'class': 'form-select'
            }),
            'foto': forms.ClearableFileInput(attrs={
                'class': 'form-control', 'onchange': 'previewImage(event)'
            }),
        }

    # Validación personalizada
    def clean_fecha_nacimiento(self): 
        fecha = self.cleaned_data['fecha_nacimiento']
        if fecha > date.today():
            raise ValidationError("La fecha no puede ser futura.")
        return fecha


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['titulo', 'contenido', 'importante']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'importante': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        

