"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from general.views import Index

from reportes.views import MensualesList, ReporteDetail, AnualesList, Reporte_anualDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),

    path('', Index, name='Index'),

    path('reportes/mensuales/', MensualesList, name='Mensuales'),
    path('reportes/mensuales/<int:pk>/', ReporteDetail, name='Reporte'),

    path('reportes/anuales/', AnualesList, name='Anuales'),
    path('reportes/anual/<int:pk>/', Reporte_anualDetail, name='Reporte_anual'),
]
