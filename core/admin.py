from django.contrib import admin
from .models import (
    Interno, FamiliarResponsables, ConsultaMedica, AgendaCita, 
    FichaMedica, RecetaMedica, InsumoInventario, Donacion, 
    GastoOperativo, PagoFundacion
)

# Configuración personalizada del sitio de administración
admin.site.site_header = "Administración Asilo Cabeza de Algodón"
admin.site.site_title = "Asilo Cabeza de Algodón"
admin.site.index_title = "Gestión Integral del Sistema"

@admin.register(Interno)
class InternoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'dpi', 'habitacion', 'estado')
    list_filter = ('estado', 'habitacion')
    search_fields = ('nombre', 'apellido', 'dpi')

@admin.register(FamiliarResponsables)
class FamiliarResponsablesAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'parentesco', 'telefono', 'interno')
    search_fields = ('nombre_completo', 'interno__nombre', 'interno__apellido')

@admin.register(ConsultaMedica)
class ConsultaMedicaAdmin(admin.ModelAdmin):
    list_display = ('interno', 'fecha', 'medico_cargo', 'diagnostico')
    list_filter = ('fecha',)
    search_fields = ('interno__nombre', 'medico_cargo')

@admin.register(AgendaCita)
class AgendaCitaAdmin(admin.ModelAdmin):
    list_display = ('interno', 'fecha_hora_cita', 'medico_especialista', 'estado_cita')
    list_filter = ('estado_cita', 'fecha_hora_cita')
    search_fields = ('interno__nombre', 'medico_especialista')

@admin.register(FichaMedica)
class FichaMedicaAdmin(admin.ModelAdmin):
    list_display = ('interno', 'tipo_sangre', 'alergias', 'padecimientos_cronicos')
    search_fields = ('interno__nombre', 'interno__apellido')

@admin.register(RecetaMedica)
class RecetaMedicaAdmin(admin.ModelAdmin):
    list_display = ('interno', 'medicamento', 'dosis', 'frecuencia')
    search_fields = ('interno__nombre', 'medicamento')

@admin.register(InsumoInventario)
class InsumoInventarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_insumo', 'categoria', 'cantidad_disponible', 'unidad_medida')
    list_filter = ('categoria',)
    search_fields = ('nombre_insumo',)

@admin.register(Donacion)
class DonacionAdmin(admin.ModelAdmin):
    list_display = ('donante', 'monto', 'tipo_donacion', 'fecha')
    list_filter = ('tipo_donacion', 'fecha')
    search_fields = ('donante',)

@admin.register(GastoOperativo)
class GastoOperativoAdmin(admin.ModelAdmin):
    list_display = ('concepto', 'monto', 'categoria', 'fecha')
    list_filter = ('categoria', 'fecha')
    search_fields = ('concepto',)

@admin.register(PagoFundacion)
class PagoFundacionAdmin(admin.ModelAdmin):
    list_display = ('concepto', 'monto', 'fecha_pago', 'comprobante')
    list_filter = ('fecha_pago',)