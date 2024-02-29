from django.db import models

from general.models import Reporte, Año

# Create your models here.

class Fijo(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    concepto = models.CharField(max_length=500)
    cantidad = models.FloatField()
    año = models.ForeignKey(Año, on_delete=models.CASCADE)
    mes = models.ForeignKey(Reporte, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural ='Gastos Fijos'

    def __str__(self):
        return r'{} / {}'.format(self.mes, self.concepto) 

class Variable(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    concepto = models.TextField()
    cantidad = models.FloatField()
    año = models.ForeignKey(Año, on_delete=models.CASCADE)
    mes = models.ForeignKey(Reporte, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural ='Gastos Variables'

    def __str__(self):
        return r'{} / {}'.format(self.mes, self.concepto) 
