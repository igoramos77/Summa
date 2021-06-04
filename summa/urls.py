from django.urls import path

from . views import IndexView, CertificadoView, MeusEnviosView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('certificado', CertificadoView.as_view(), name='certificado'),
    path('meus-envios', MeusEnviosView.as_view(), name='meus-envios'),
]
