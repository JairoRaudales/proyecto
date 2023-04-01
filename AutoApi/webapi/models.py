from django.db import models

# Create your models here.
class TipoAuto(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self) :
        return self.descripcion
    
class Marca(models.Model):
    descripcion = models.CharField(max_length=200)
    id_tipo_Auto = models.ForeignKey(TipoAuto, on_delete=models.CASCADE)

    def __str__(self) :
        return self.descripcion
    
class Modelo(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion
    
class Color(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion
    
class Estado(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion
    
class Genero(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion
  
    
class Auto(models.Model):
    descripcion = models.CharField(max_length=200)
    id_tipo_Auto = models.ForeignKey(TipoAuto, on_delete=models.CASCADE)
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    id_modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    precio = models.CharField(max_length=200)
    año = models.CharField(max_length=200)
    observaciones = models.CharField(max_length=200)

    def __str__(self):
        return self.id_tipo_Auto
    
class Cliente(models.Model):
    id_nacional = models.CharField(max_length=60)
    nombre = models.CharField(max_length=200)
    apelllido = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField
    email = models.EmailField

    def __str__(self):
        return self.nombre + " " + self.apelllido

class AutoColor(models.Model):
    descripcion = models.CharField(max_length=200)
    id_Color = models.ForeignKey(Color, on_delete=models.CASCADE)
    id_Auto = models.ForeignKey(Auto, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion  