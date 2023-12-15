from django import forms
from .models import Store

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'  # Esto incluirá todos los campos de tu modelo Store en el formulario