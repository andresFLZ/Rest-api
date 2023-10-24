from django import forms
from api.models import Tutorial

class TutorialForm(forms.ModelForm):
    # Formulario que hace referencia al modelo Tutorial
    
    class Meta:
        model = Tutorial
        fields = "__all__"