from django.contrib import admin

from .models import Llamado, Asignatura
# Register your models here.

class LlamadoAdmin(admin.ModelAdmin):
    list_display = ('tipo_llamado', 'cargo', 'dedicacion', 'display_asignatura', 'fecha_apertura', 'fecha_cierre', 'is_public')
    list_editable = ('is_public',)
    list_filter = ('is_public', 'tipo_llamado')

admin.site.register(Llamado, LlamadoAdmin)
admin.site.register(Asignatura)