from django.contrib import admin
from .models import (
    Interno, FamiliarResponsable, ConsultaMedica, AgendaCita, 
    Donacion, GastoOperativo, PagoFundacion
)

# Configuración personalizada del sitio de administración
admin.site.site_header = "Administración Asilo Cabeza de Algodón"
admin.site.site_title = "Asilo Cabeza de Algodón"
admin.site.index_title = "Gestión Integral del Sistema"

# Registros sencillos y a prueba de errores de campo
admin.site.register(Interno)
admin.site.register(FamiliarResponsable)
admin.site.register(ConsultaMedica)
admin.site.register(AgendaCita)
admin.site.register(Donacion)
admin.site.register(GastoOperativo)
admin.site.register(PagoFundacion)