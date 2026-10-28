from django import forms
from .models import Interno

class InternoForm(forms.ModelForm):
    class Meta:
        model = Interno
        # Pon solo los campos esenciales que ya están creados en la BD de producción
        fields = ['nombre_completo', 'fecha_nacimiento', 'motivo_reclusion', 'estado']