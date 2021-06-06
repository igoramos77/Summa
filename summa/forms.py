from django.forms import ModelForm
from summa.models import AtividadeComplementar
class AtividadeComplementarForm(ModelForm):
    class Meta:
        model = AtividadeComplementar
        fields = "__all__"
