from django.forms import ModelForm
from django.contrib.auth import forms
from summa.models import AtividadeComplementar, Usuario


class AtividadeComplementarForm(ModelForm):
    class Meta:
        model = AtividadeComplementar
        fields = ['usuario', 'curso', 'descricao', 'categoria', 'cnpj', 'empresa', 'carga_horaria_informada', 'certificado']


class ProfileForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'foto']


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Usuario


class ChangePassword(forms.PasswordChangeForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Usuario
