from django.db import models

from general.models import Edificio, Departamento, Reporte, Estado, Año

# Create your models here.

class Pago(models.Model):
    created = models.DateTimeField(auto_now=True)
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE) 
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    corbatin_folio = models.CharField(max_length=24, blank=True, null=True)
    año = models.ForeignKey(Año, on_delete=models.CASCADE)
    mes = models.ForeignKey( Reporte, on_delete=models.CASCADE) 
    status = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return r'{}'.format(self.id)
