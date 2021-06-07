from django.forms import ModelForm
from summa.models import AtividadeComplementar, Usuario


class AtividadeComplementarForm(ModelForm):
    class Meta:
        model = AtividadeComplementar
        fields = "__all__"


class ProfileForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

