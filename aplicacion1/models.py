from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=5,decimal_places=2)
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_p = models.CharField(max_length=30)
    apellido_m = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=13)
    
    def __str__(self):
        return self.nombre


