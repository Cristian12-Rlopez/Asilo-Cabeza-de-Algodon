from django.contrib import admin
from .models import Interno, FamiliarResponsable, VisitaMedica, PagoFundacion, MovimientoFinanciero

# Personalización del título del Panel Administrativo
admin.site.site_header = "Asilo Cabeza de Algodón - Administración"
admin.site.site_title = "Portal Administrativo"
admin.site.index_title = "Gestión del Sistema"

# Registro de modelos para acceso total del administrador
admin.site.register(Interno)
admin.site.register(FamiliarResponsable)
admin.site.register(VisitaMedica)
admin.site.register(PagoFundacion)
admin.site.register(MovimientoFinanciero)
# Register your models here.
