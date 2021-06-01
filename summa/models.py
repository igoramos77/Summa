from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from uuid import uuid4
from summa.manager import UserManager


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return filename


class Destination(models.Model):
    place = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')


class CategoriaAtividadeComplementar(models.Model):
    external_id = models.UUIDField(default=uuid4, editable=False)
    macroatividades = models.CharField('Macroatividades', max_length=55)
    carga_horaria_maxima_categoria = models.IntegerField('Carga Horária Máxima da Categoria para este Curso')
    descricao = models.TextField('Descrição', max_length=500, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria Atividade Complementar'
        verbose_name_plural = 'Categorias Atividades Complementares'
        ordering = ['id']

    def __str__(self):
        return f"{self.macroatividades}"


class Estado(models.Model):
    external_id = models.UUIDField(default=uuid4, editable=False)
    uf = models.CharField('UF', unique=True, max_length=2)
    estado = models.CharField('Estado', max_length=55)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['id']

    def __str__(self):
        return f"{self.uf} / {self.estado}"


class Instituicao(models.Model):
    external_id = models.UUIDField(default=uuid4, editable=False)
    nome = models.CharField('Nome', max_length=255)

    class Meta:
        verbose_name = 'Instituição'
        verbose_name_plural = 'Instituições'
        ordering = ['id']

    def __str__(self):
        return f"{self.nome}"


class Campus(models.Model):
    external_id = models.UUIDField(default=uuid4, editable=False)
    cep = models.CharField('CEP', max_length=9)
    logradouro = models.CharField('Logradouro', max_length=255)
    numero = models.CharField('Numero', max_length=9)
    complemento = models.CharField('Complemento', max_length=255, blank=True)
    bairro = models.CharField('Bairro', max_length=55)
    cidade = models.CharField('Cidade', max_length=55)
    estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING)
    instituicao = models.ForeignKey(Instituicao, related_name='campus', on_delete=models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Campus'
        verbose_name_plural = 'Campus'
        ordering = ['id']

    def __str__(self):
        return f"{self.instituicao} / {self.cidade} / {self.estado}"


class Curso(models.Model):
    external_id = models.UUIDField(default=uuid4, editable=False)
    nome = models.CharField('Nome', max_length=55)
    minimo_categorias = models.IntegerField('Quantidade Mínima de Categorias')
    campus = models.ForeignKey(Campus, on_delete=models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']

    def __str__(self):
        return f"{self.nome}"


#   Classe associativa
class CategoriaCurso(models.Model):
    external_id = models.UUIDField(default=uuid4, editable=False)
    curso = models.ForeignKey(Curso, null=True, on_delete=models.DO_NOTHING)
    categoria_atividade_complementar = models.ManyToManyField(CategoriaAtividadeComplementar)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria Curso'
        verbose_name_plural = 'Categorias Cursos'
        ordering = ['id']

    def __str__(self):
        return f"{self.categoria_atividade_complementar}"


#   class Aluno(models.Model):
class Aluno(AbstractUser):
    external_id = models.UUIDField(default=uuid4, editable=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    matricula = models.CharField(unique=True, max_length=55)
    email = models.EmailField('Email', max_length=155, unique=True)
    foto = models.FileField('Foto', null=True, blank=True, upload_to=get_file_path)
    curso = models.ForeignKey(Curso, blank=True, null=True, on_delete=models.DO_NOTHING)

    objects = UserManager()

    USERNAME_FIELD = 'matricula'

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['id']

    def __str__(self):
        return f"{self.matricula}"


class Empresa(models.Model):
    cnpj = models.IntegerField('CNPJ', primary_key=True)
    razao_social = models.CharField('Razão Social', max_length=255)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=155, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=16, null=True, blank=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['razao_social']

    def __str__(self):
        return f"{self.cnpj} / {self.razao_social}"


class AtividadeComplementar(models.Model):
    external_id = models.UUIDField(default=uuid4, editable=False)
    aluno = models.ForeignKey(Aluno, null=True, related_name='aluno', on_delete=models.DO_NOTHING)
    categoria = models.ForeignKey(CategoriaAtividadeComplementar, on_delete=models.DO_NOTHING)
    descricao = models.CharField('Descrição', max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    carga_horaria_informada = models.IntegerField('Carga Horária Informada')
    carga_horaria_integralizada = models.IntegerField('Carga Horária Integralizada', null=True, blank=True)
    justificativa = models.TextField('justificativa', max_length=500, blank=True, null=True)
    certificado_img = models.FileField('Certificado', null=True, blank=True, upload_to=get_file_path)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Atividade Complementar'
        verbose_name_plural = 'Atividades Complementares'
        ordering = ['id']

    def __str__(self):
        return f"{self.descricao} / {self.carga_horaria_informada}"
