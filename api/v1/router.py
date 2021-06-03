from django.urls import include, path
from rest_framework import routers

from .viewsets import (AtividadeComplementarViewSet, CampusViewSet,
                       CategoriaAtividadeComplementarViewSet,
                       CategoriaCursoViewSet, CursoViewSet, EmpresaViewSet,
                       EstadoViewSet, InstituicaoViewSet, UsuarioViewSet)

router = routers.DefaultRouter()
router.register(r'atividades-complementares', AtividadeComplementarViewSet)
router.register(r'campi', CampusViewSet)
router.register(r'categorias-atividade-complementar',
                CategoriaAtividadeComplementarViewSet)
router.register(r'categorias-curso', CategoriaCursoViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'estados', EstadoViewSet)
router.register(r'instituicoes', InstituicaoViewSet)
router.register(r'usuarios', UsuarioViewSet)
