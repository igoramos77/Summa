from django.urls import path

from . views import IndexView, CertificadoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('certificado', CertificadoView.as_view(), name='certificado'),
]
