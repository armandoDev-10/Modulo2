from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Fijo,Variable

# Register your models here.

@admin.register(Fijo)
class FijoAdmin(ImportExportModelAdmin):
    pass

@admin.register(Variable)
class VariableAdmin(ImportExportModelAdmin):
    pass
