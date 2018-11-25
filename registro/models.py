from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    correo = models.CharField(max_length=40)
    contrasenia = models.CharField(max_length=40)
    foto = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return "PERSONA"

class Articulo(models.Model):
    nameD = models.CharField(max_length=40)
    cantidad = models.CharField(max_length=40)
    desc = models.CharField(max_length=40)
    fotoD = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return "ARTICULO"