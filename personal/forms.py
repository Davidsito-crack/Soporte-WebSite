from django import forms
from .models import comodatos
from personal.models import people

class comodatosForm(forms.ModelForm):
    class Meta:
        model = comodatos
        fields = ['comodato']