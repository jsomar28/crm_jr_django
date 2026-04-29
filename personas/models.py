from django.db import models
from django.conf import settings
# from .models import Persona

class Persona(models.Model):

    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('ventas', 'Ventas'),
        ('operador', 'Operador'),
    )

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    direccion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    rol = models.CharField(max_length=20, choices=ROLE_CHOICES, default='operador')

    foto = models.ImageField(upload_to='personas/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"




class Nota(models.Model):
    persona = models.ForeignKey(
        Persona, 
        on_delete=models.CASCADE, 
        related_name='notas'
    )

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()

    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    importante = models.BooleanField(default=False)

    class Meta:
        ordering =['-importante', '-fecha_actualizacion']

    def __str__(self):
        return f"{self.titulo} - {self.persona.nombre}"