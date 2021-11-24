from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from summa.models import (AtividadeComplementar, Campus,
                          CategoriaAtividadeComplementar,
                          Curso, Estado, Instituicao, Usuario)

from .serializers import (AtividadeComplementarSerializer, CampusSerializer,
                          CategoriaAtividadeComplementarSerializer, CursoSerializer,
                          EstadoSerializer,
                          InstituicaoSerializer, UsuarioSerializer)


class AtividadeComplementarViewSet(viewsets.ModelViewSet):
    queryset = AtividadeComplementar.objects.all()
    serializer_class = AtividadeComplementarSerializer

    @action(detail=True, methods=['get'])
    def usuario(self, request, pk=None):
        atividade_complementar = self.get_object()
        serializer = UsuarioSerializer(atividade_complementar.usuario, many=False)
        return Response(serializer.data)


class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer


class CategoriaAtividadeComplementarViewSet(viewsets.ModelViewSet):
    queryset = CategoriaAtividadeComplementar.objects.all()
    serializer_class = CategoriaAtividadeComplementarSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


class InstituicaoViewSet(viewsets.ModelViewSet):
    queryset = Instituicao.objects.all()
    serializer_class = InstituicaoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @action(detail=True, methods=['get'])
    def atividades(self, request, pk=None):
        atividades_complementares = self.get_object()
        serializer = AtividadeComplementarSerializer(atividades_complementares.usuario.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def count(self, request, pk=None):
        usuario_id = pk
        queryset = AtividadeComplementar.objects.raw(
            "SELECT * FROM summa_atividadecomplementar WHERE usuario_id = %s", [usuario_id])
        serializer = AtividadeComplementarSerializer(queryset, many=True)
        return Response(serializer.data)
