from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Remanente, Recuperadas

# Register your models here.

@admin.register(Remanente)
class RemanenteAdmin(ImportExportModelAdmin):
    pass

@admin.register(Recuperadas)
class RecuperadasAdmin(ImportExportModelAdmin):
    pass
