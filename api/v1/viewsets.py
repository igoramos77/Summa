from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db import connection

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


def dictfetchall(cursor):
    #    Return all rows from a cursor as a dict
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @action(detail=True, methods=['get'])
    def atividades(self, request, pk=None):
        atividades_complementares = self.get_object()
        serializer = AtividadeComplementarSerializer(atividades_complementares.usuario.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'], url_path='total-horas-integralizadas')
    def total_ingralizadas(self, request, pk=None):
        with connection.cursor() as cursor:
            cursor.execute("SELECT SUM(carga_horaria_integralizada) as total_horas_integralizadas FROM summa_atividadecomplementar WHERE usuario_id = %s", [pk])
            row = dictfetchall(cursor)

        return Response(row)

    @action(detail=True, methods=['GET'], url_path='total-atividades-submetidas')
    def total_submetidas(self, request, pk=None):
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(id) as atividades_submetidas FROM summa_atividadecomplementar WHERE usuario_id = %s", [pk])
            row = dictfetchall(cursor)

        return Response(row)

    @action(detail=True, methods=['GET'], url_path='total-aguardando-validacao')
    def aguardando_validacao(self, request, pk=None):
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(id) as atividades_aguardando_validacao FROM summa_atividadecomplementar WHERE status = 'em_validação' AND usuario_id = %s", [pk])
            row = dictfetchall(cursor)

        return Response(row)

    @action(detail=True, methods=['GET'], url_path='total-recusadas')
    def aguardando_recusadas(self, request, pk=None):
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(id) as atividades_recusadas FROM summa_atividadecomplementar WHERE status = 'recusado' AND usuario_id = %s", [pk])
            row = dictfetchall(cursor)

        return Response(row)
