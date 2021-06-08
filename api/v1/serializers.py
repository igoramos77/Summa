from rest_framework import serializers
from summa.models import (AtividadeComplementar, Campus,
                          CategoriaAtividadeComplementar,
                          Curso, Estado, Instituicao, Usuario)


class AtividadeComplementarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtividadeComplementar
        fields = '__all__'


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = '__all__'


class CategoriaAtividadeComplementarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaAtividadeComplementar
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'


class InstituicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituicao
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
