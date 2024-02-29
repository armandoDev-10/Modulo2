from django.db import models

# Create your models here.

class DatosAdmin(models.Model):
    created = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=264)
    fecha_de_inicio = models.DateField()
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Año(models.Model):
    created = models.DateTimeField(auto_now=True)
    año = models.IntegerField()
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Año del ejercicio'
    
    def __str__(self):
        return r'{}'.format(self.año)

class Estado(models.Model):
    created = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=64)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.estado
    
class Edificio(models.Model):
    created = models.DateTimeField(auto_now=True)
    edificio = models.CharField(max_length=3)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.edificio

class Departamento(models.Model):
    created = models.DateTimeField(auto_now=True)
    departamento = models.CharField(max_length=3)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.departamento

class Reporte(models.Model):
    created = models.DateTimeField(auto_now=True)
    año = models.ForeignKey(Año, on_delete=models.CASCADE)
    mes = models.CharField(max_length=64)
    aportacion = models.FloatField(default=0)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mes
