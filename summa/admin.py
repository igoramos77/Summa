from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from summa.forms import UserChangeForm, UserCreationForm

from summa import models

from summa.models import Usuario


@admin.register(models.Usuario)
class UsuarioAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Usuario
    list_display = ('id', 'matricula')
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Informações Pessoais", {"fields": ("external_id", "matricula", "foto", "curso")}),
    )


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
    search_fields = ('id', 'nome')
    list_filter = ('nome',)
    list_per_page = 15


@admin.register(models.CategoriaAtividadeComplementar)
class CategoriaAtividadeComplementarAdmin(admin.ModelAdmin):
    list_display = ('id', 'macroatividades', 'create_at')


@admin.register(models.AtividadeComplementar)
class AtividadeComplementarAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'usuario', 'curso', 'carga_horaria_informada', 'carga_horaria_integralizada', 'status', 'is_active', 'create_at')
    search_fields = ('id', 'descricao', 'status')
    list_filter = ('status', 'create_at')
    list_per_page = 15

