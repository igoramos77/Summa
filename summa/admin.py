from __future__ import unicode_literals

from django.contrib import admin
from . import models


@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'matricula', 'create_at')


@admin.register(models.Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'uf')


@admin.register(models.Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


@admin.register(models.Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('instituicao', 'cidade', 'create_at')


@admin.register(models.Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'create_at')


@admin.register(models.CategoriaAtividadeComplementar)
class CategoriaAtividadeComplementarAdmin(admin.ModelAdmin):
    list_display = ('id', 'macroatividades', 'create_at')


@admin.register(models.CategoriaCurso)
class CategoriaCursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'curso', 'create_at')


@admin.register(models.AtividadeComplementar)
class AtividadeComplementarAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'carga_horaria_informada', 'carga_horaria_integralizada', 'create_at')


@admin.register(models.Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'razao_social')
