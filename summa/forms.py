from django.forms import ModelForm
from summa.models import AtividadeComplementar


class AtividadeComplementarForm(ModelForm):
    class Meta:
        model = AtividadeComplementar
        #   fields = "__all__"
        fields = ('usuario', 'categoria', 'descricao', 'empresa', 'carga_horaria_informada', 'carga_horaria_integralizada', 'justificativa', 'certificado', 'status', 'is_active')
