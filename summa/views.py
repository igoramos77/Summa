from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, FormView, ListView

from django.db.models import Sum
from django.urls import reverse_lazy

from django.db.models.functions import TruncMonth, ExtractDay, ExtractMonth, ExtractYear
from django.db.models import Count

from datetime import datetime

from summa.models import Usuario, AtividadeComplementar, Curso

from summa.forms import AtividadeComplementarForm, ProfileForm, UserChangeForm


def errorlog(request):
    messages.info(request, "Please login to view the content")
    return redirect("/")


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['current_user'] = Usuario.objects.get(matricula=self.request.user)

        context['total_atividades_submetidas'] = AtividadeComplementar.objects.filter(usuario=context['current_user']).count()

        context['total_atividades_aguardando_aprovacao'] = AtividadeComplementar.objects.filter(usuario=context['current_user'], status='em validação').count()

        context['total_atividades_recusadas'] = AtividadeComplementar.objects.filter(usuario=context['current_user'], status='recusado').count()

        if AtividadeComplementar.objects.filter(usuario=context['current_user'], status='aprovado').aggregate(Sum('carga_horaria_integralizada')).get('carga_horaria_integralizada__sum', 0.00) is None:
            context['total_horas_integralizadas'] = 0
        else:
            context['total_horas_integralizadas'] = AtividadeComplementar.objects.filter(usuario=context['current_user'], status='aprovado').aggregate(Sum('carga_horaria_integralizada')).get('carga_horaria_integralizada__sum', 0.00)

        context['qtd_min_horas'] = Curso.objects.values_list('qtd_horas_conclusao', flat=True).filter(usuario__matricula=context['current_user']).first()

        if context['total_horas_integralizadas'] is not None:
            context['percent_conslusion'] = context['total_horas_integralizadas'] * 100 / context['qtd_min_horas']
        else:
            context['percent_conslusion'] = 0

        context['list_atividades_complementares'] = AtividadeComplementar.objects.filter(usuario=context['current_user']).all().order_by('-create_at')[:5]

        context['list_group_atividades_complementares'] = AtividadeComplementar.objects \
                                                        .filter(usuario=context['current_user']) \
                                                        .values('categoria__macroatividades') \
                                                        .annotate(count=Count('categoria__macroatividades')).order_by() \
                                                        .values('categoria__macroatividades', 'count')[:5]

        context['data_graph_months'] = AtividadeComplementar.objects \
            .extra({"date": """strftime('%%m/%%Y', create_at)"""}) \
            .filter(usuario=context['current_user'], carga_horaria_integralizada__gt=0) \
            .annotate(month=ExtractMonth('create_at')).order_by() \
            .values('date') \
            .annotate(total=Count('*')) \

        for test in context['data_graph_months']:
            test['date'] = datetime.strptime(test['date'], '%m/%Y')

        context['data_graph_hours'] = AtividadeComplementar.objects\
            .extra({"date": """strftime('%%m/%%Y', create_at)"""}) \
            .filter(usuario=context['current_user'], carga_horaria_integralizada__gt=0) \
            .annotate(month=ExtractMonth('create_at')).order_by() \
            .values('date') \
            .annotate(total=Sum('carga_horaria_integralizada'))

        for test in context['data_graph_hours']:
            test['date'] = datetime.strptime(test['date'], '%m/%Y')

        #   form
        context['form_add_atividade_complementar'] = AtividadeComplementarForm() 

        return context


class CertificadoView(TemplateView):
    template_name = 'certificado.html'

    def get_context_data(self, **kwargs):
        context = super(CertificadoView, self).get_context_data(**kwargs)

        context['current_user'] = Usuario.objects.get(matricula=self.request.user)
        context['total_atividades_submetidas'] = AtividadeComplementar.objects.filter(usuario=context['current_user']).count()

        context['total_horas_integralizadas'] = AtividadeComplementar.objects.filter(usuario=context['current_user'], status='aprovado').aggregate(Sum('carga_horaria_integralizada')).get('carga_horaria_integralizada__sum', 0.00)

        context['qtd_min_horas'] = Curso.objects.values_list('qtd_horas_conclusao', flat=True).filter(usuario__matricula=context['current_user']).first()

        return context


class MeusEnviosView(ListView):
    template_name = 'meus-envios.html'
    paginate_by = 6
    ordering = ['id']
    model = AtividadeComplementar

    def get_context_data(self, **kwargs):
        context = super(MeusEnviosView, self).get_context_data(**kwargs)

        context['current_user'] = Usuario.objects.get(matricula=self.request.user)

        context['total_atividades_submetidas'] = AtividadeComplementar.objects.filter(usuario=context['current_user']).count()
        if AtividadeComplementar.objects.filter(usuario=context['current_user'], status='aprovado').aggregate(Sum('carga_horaria_integralizada')).get('carga_horaria_integralizada__sum', 0.00) is None:
            context['total_horas_integralizadas'] = 0
        else:
            context['total_horas_integralizadas'] = AtividadeComplementar.objects.filter(usuario=context['current_user'], status='aprovado').aggregate(Sum('carga_horaria_integralizada')).get('carga_horaria_integralizada__sum', 0.00)

        context['qtd_min_horas'] = Curso.objects.values_list('qtd_horas_conclusao', flat=True).filter(usuario__matricula=context['current_user']).first()

        if context['total_horas_integralizadas'] is not None:
            context['percent_conslusion'] = context['total_horas_integralizadas'] * 100 / context['qtd_min_horas']
        else:
            context['percent_conslusion'] = 0

        context['list_atividades_complementares'] = AtividadeComplementar.objects.filter(usuario=context['current_user']).all().order_by('-create_at')

        return context

    def get_queryset(self, **kwargs):
        current_user = Usuario.objects.get(matricula=self.request.user)
        return AtividadeComplementar.objects.filter(usuario=current_user).all().order_by('-create_at')


class SubmeterCertificadoView(FormView):
    template_name = 'enviar-certificado.html'
    form_class = AtividadeComplementarForm
    success_url = reverse_lazy('meus-envios')

    def get_context_data(self, **kwargs):
        context = super(SubmeterCertificadoView, self).get_context_data(**kwargs)

        context['current_user'] = Usuario.objects.get(matricula=self.request.user)

        context['total_atividades_submetidas'] = AtividadeComplementar.objects.filter(
            usuario=context['current_user']).count()
        if AtividadeComplementar.objects.filter(usuario=context['current_user'], status='aprovado').aggregate(
                Sum('carga_horaria_integralizada')).get('carga_horaria_integralizada__sum', 0.00) is None:
            context['total_horas_integralizadas'] = 0
        else:
            context['total_horas_integralizadas'] = AtividadeComplementar.objects.filter(
                usuario=context['current_user'], status='aprovado').aggregate(Sum('carga_horaria_integralizada')).get(
                'carga_horaria_integralizada__sum', 0.00)

        context['qtd_min_horas'] = Curso.objects.values_list('qtd_horas_conclusao', flat=True).filter(
            usuario__matricula=context['current_user']).first()

        if context['total_horas_integralizadas'] is not None:
            context['percent_conslusion'] = context['total_horas_integralizadas'] * 100 / context['qtd_min_horas']
        else:
            context['percent_conslusion'] = 0
        
        #   form
        context['form_add_atividade_complementar'] = AtividadeComplementarForm()
        return context

    def form_valid(self, form, *args, **kwargs):
        instance = form.save(commit=False)
        instance.save()
        messages.success(self.request, 'Atividade Complementar enviada com sucesso! 👌', extra_tags='success')
        return super(SubmeterCertificadoView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Falha ao submeter o certificado. 😢', extra_tags='danger')
        return super(SubmeterCertificadoView, self).form_invalid(form, *args, **kwargs)


class PerfilView(FormView):
    template_name = 'perfil.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('perfil')

    def get_context_data(self, **kwargs):
        context = super(PerfilView, self).get_context_data(**kwargs)

        context['current_user'] = Usuario.objects.get(matricula=self.request.user)

        context['total_atividades_submetidas'] = AtividadeComplementar.objects.filter(
            usuario=context['current_user']).count()
        if AtividadeComplementar.objects.filter(usuario=context['current_user'], status='aprovado').aggregate(
                Sum('carga_horaria_integralizada')).get('carga_horaria_integralizada__sum', 0.00) is None:
            context['total_horas_integralizadas'] = 0
        else:
            context['total_horas_integralizadas'] = AtividadeComplementar.objects.filter(
                usuario=context['current_user'], status='aprovado').aggregate(Sum('carga_horaria_integralizada')).get(
                'carga_horaria_integralizada__sum', 0.00)

        context['qtd_min_horas'] = Curso.objects.values_list('qtd_horas_conclusao', flat=True).filter(
            usuario__matricula=context['current_user']).first()

        if context['total_horas_integralizadas'] is not None:
            context['percent_conslusion'] = context['total_horas_integralizadas'] * 100 / context['qtd_min_horas']
        else:
            context['percent_conslusion'] = 0

        #   Profile form
        context['form_edit_profile'] = UserChangeForm(self.request.POST or None, instance=self.request.user)

        return context

    def post(self, *args, **kwargs):
        form = UserChangeForm(self.request.POST or None, self.request.FILES, instance=self.request.user)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Perfil autalizado com sucesso! 👌', extra_tags='success')
            return super(PerfilView, self).form_valid(form)
        messages.error(self.request, 'Poxa, algo deu errado. 😢', extra_tags='danger')
        return super(PerfilView, self).form_valid(form)
