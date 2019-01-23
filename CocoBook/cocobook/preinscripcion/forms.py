from django import forms
from preinscripcion.models import PlanPreIns, UsuarioPreIns

class nuevoInscritoForm(forms.ModelForm):
    class Meta:
        model = UsuarioPreIns
        fields = ('nombre','email','plan_preferido')
