from django import forms
from .models import Interno

class InternoForm(forms.ModelForm):
    class Meta:
        model = Interno
        fields = '__all__' # O puedes listar los campos que necesites mostrar