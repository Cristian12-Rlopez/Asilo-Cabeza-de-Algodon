from django import forms
from .models import Interno

class InternoForm(forms.ModelForm):
    class Meta:
        model = Interno
        fields = ['nombre_completo', 'fecha_nacimiento', 'motivo_reclusion', 'habitacion', 'psicopatologias, medicinas_de_cajon'] # O puedes listar los campos que necesites mostrar