from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('panel/', views.panel_usuario, name='panel_usuario'),
]
