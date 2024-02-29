from django.db import models

from general.models import Año, Reporte, Edificio,Departamento

# Create your models here.

class Remanente(models.Model):
    create = models.DateTimeField(auto_now=True)
    cantidad = models.FloatField()
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Remanete anterior'
    
    def __str__(self):
        return r'$ {}'.format(self.cantidad)

class Recuperadas(models.Model):
    create = models.DateTimeField(auto_now=True)
    año = models.ForeignKey(Año, on_delete=models.CASCADE)
    mes = models.ForeignKey(Reporte, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    no_cuotas = models.IntegerField(default=0, null=True, blank=True)
    concepto = models.TextField()
    edificio = models.ForeignKey(Edificio,on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Cuotas Recuperadas'
    
    def __str__(self):
        return r'$ {} / {} / {}'.format(self.cantidad,self.mes, self.año)


