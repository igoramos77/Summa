from django.urls import path

from summa.views import IndexView, CertificadoView, MeusEnviosView, SubmeterCertificadoView, PerfilView, \
    AlterarSenhaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('certificado/', CertificadoView.as_view(), name='certificado'),
    path('meus-envios/', MeusEnviosView.as_view(), name='meus-envios'),
    path('enviar-certificado/', SubmeterCertificadoView.as_view(), name='enviar-certificado'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('alterar-senha/', AlterarSenhaView.as_view(), name='alterar-senha'),
]
