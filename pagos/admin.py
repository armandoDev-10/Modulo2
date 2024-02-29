from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Pago

# Register your models here.

@admin.register(Pago)
class PagoAdmin(ImportExportModelAdmin):
    list_display = ['edificio', 'departamento', 'mes', 'status']
    list_filter = ('mes', 'status')
