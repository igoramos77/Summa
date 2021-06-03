from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.db.models import Sum


from .models import Usuario, AtividadeComplementar, Curso


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

        context['graph_historico_labels'] = AtividadeComplementar.objects.filter(usuario=context['current_user']) \
                                            .all().order_by('create_at').values_list('create_at', flat=True)

        return context

    def get_labels(self):
        labels = []
        queryset = AtividadeComplementar.objects.filter(usuario=context['current_user']).all().order_by('create_at')
        for curso in queryset:
            labels.append(curso.nome)
        return labels

    def get_data(self):
        resultado = []
        dados = []
        queryset = Curso.objects.order_by('id').annotate(total=Count('aluno'))
        for linha in queryset:
            dados.append(int(linha.total))
        resultado.append(dados)
        return resultado


class CertificadoView(TemplateView):
    template_name = 'certificado.html'

    def get_context_data(self, **kwargs):
        context = super(CertificadoView, self).get_context_data(**kwargs)

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

        context['list_atividades_complementares'] = AtividadeComplementar.objects.filter(usuario=context['current_user']).all().order_by('-create_at')[:5]

        return context
