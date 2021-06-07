from django.urls import path

from summa.views import IndexView, CertificadoView, MeusEnviosView, SubmeterCertificadoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('certificado/', CertificadoView.as_view(), name='certificado'),
    path('meus-envios/(?<int:id>)', MeusEnviosView.as_view(), name='meus-envios'),
    path('enviar-certificado/', SubmeterCertificadoView.as_view(), name='enviar-certificado'),
]
