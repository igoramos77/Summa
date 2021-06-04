from django.urls import path

from summa.views import IndexView, CertificadoView, MeusEnviosView, form_send_atividade_complementar

urlpatterns = [
    #   path('', form_send_atividade_complementar, name='index'),
    path('', IndexView.as_view(), name='index'),
    path('certificado', CertificadoView.as_view(), name='certificado'),
    path('meus-envios', MeusEnviosView.as_view(), name='meus-envios'),
]
