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

        if AtividadeComplementar.objects.filter(usuario=context['current_user'], status='aprovado').aggregate(Sum('carga_horaria_integralizada')).get('carga_horaria_integralizada__sum', 0.00) is None:
            context['total_horas_integralizadas'] = 0
        else:
            context['total_horas_integralizadas'] = AtividadeComplementar.objects.filter(usuario=context['current_user'], status='aprovado').aggregate(Sum('carga_horaria_integralizada')).get('carga_horaria_integralizada__sum', 0.00)

        context['qtd_min_horas'] = Curso.objects.values_list('qtd_horas_conclusao', flat=True).filter(usuario__matricula=context['current_user']).first()

        if context['total_horas_integralizadas'] is not None:
            context['percent_conslusion'] = context['total_horas_integralizadas'] * 100 / context['qtd_min_horas']
        else:
            context['percent_conslusion'] = 0

        context['list_atividades_complementares'] = AtividadeComplementar.objects.filter(usuario=context['current_user']).all()[:5]

        return context
