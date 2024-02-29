from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import DatosAdmin, Estado, Edificio, Departamento, Reporte, Año

# Register your models here.

@admin.register(DatosAdmin)
class Datos(ImportExportModelAdmin):
    pass

@admin.register(Año)
class AñoAdmin(ImportExportModelAdmin):
    pass

@admin.register(Estado)
class EstadoAdmin(ImportExportModelAdmin):
    pass

@admin.register(Edificio)
class EdificioAdmin(ImportExportModelAdmin):
    pass

@admin.register(Departamento)
class DepartamentoAdmin(ImportExportModelAdmin):
    pass

@admin.register(Reporte)
class ReporteAdmin(ImportExportModelAdmin):
    pass
