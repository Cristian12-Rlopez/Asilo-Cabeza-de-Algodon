from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import (
    dashboard_view,
    expedientes_view,
    motivos_reclusion_view,
    ficha_medica_view,
    psicopatologias_view,
    historial_clinico_view,
    evaluaciones_iniciales_view,
    remisiones_web_view,
    asignacion_enfermeros_view,
    agenda_citas_view,
    notificacion_smtp_view,
)  # <--- Aquí cerramos correctamente el paréntesis de las importaciones

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('expedientes/', expedientes_view, name='expedientes_generales'),
    path('motivos-reclusion/', motivos_reclusion_view, name='motivos_reclusion'),
    path('ficha-medica/', ficha_medica_view, name='ficha_medica'),
    path('psicopatologias/', psicopatologias_view, name='registro_psicopatologias'),
    path('historial-clinico/', historial_clinico_view, name='historial_clinico'),
    path('evaluaciones-iniciales/', evaluaciones_iniciales_view, name='evaluaciones_iniciales'),
    path('remisiones-web/', remisiones_web_view, name='remisiones_web'),
    path('asignacion-enfermeros/', asignacion_enfermeros_view, name='asignacion_enfermeros'),
    path('agenda-citas/', agenda_citas_view, name='agenda_citas'),
    path('notificacion-smtp/', notificacion_smtp_view, name='notificacion_smtp'),
]