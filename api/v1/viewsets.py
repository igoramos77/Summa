from rest_framework import viewsets
from summa.models import (AtividadeComplementar, Campus,
                          CategoriaAtividadeComplementar, CategoriaCurso,
                          Curso, Empresa, Estado, Instituicao, Usuario)

from .serializers import (AtividadeComplementarSerializer, CampusSerializer,
                          CategoriaAtividadeComplementarSerializer,
                          CategoriaCursoSerializer, CursoSerializer,
                          EmpresaSerializer, EstadoSerializer,
                          InstituicaoSerializer, UsuarioSerializer)


class AtividadeComplementarViewSet(viewsets.ModelViewSet):
    queryset = AtividadeComplementar.objects.all()
    serializer_class = AtividadeComplementarSerializer


class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer


class CategoriaAtividadeComplementarViewSet(viewsets.ModelViewSet):
    queryset = CategoriaAtividadeComplementar.objects.all()
    serializer_class = CategoriaAtividadeComplementarSerializer


class CategoriaCursoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaCurso.objects.all()
    serializer_class = CategoriaCursoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


class InstituicaoViewSet(viewsets.ModelViewSet):
    queryset = Instituicao.objects.all()
    serializer_class = InstituicaoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
