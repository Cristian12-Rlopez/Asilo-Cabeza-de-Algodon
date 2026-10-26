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
    historial_clinico_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ruta del Login apuntando a nuestra plantilla personalizada
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('expedientes/', expedientes_view, name='expedientes_generales'),
    path('motivos-reclusion/', motivos_reclusion_view, name='motivos_reclusion'),
    path('ficha-medica/', ficha_medica_view, name='ficha_medica'),
    path('psicopatologias/', psicopatologias_view, name='registro_psicopatologias'),
    path('historial-clinico/', historial_clinico_view, name='historial_clinico'),
]