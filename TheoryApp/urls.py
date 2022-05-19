"""TheoryApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from BVATApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('statistiek', views.statistiek, name='Statistiek'),
    path('help', views.help_view, name='Help'),
    path('speelscherm-tijd', views.speelscherm_tijd, name='speelscherm-tijd'),
    path('speelscherm-woorden', views.speelscherm_woorden, name='speelscherm-woorden'),
    path('instellingen-database/', views.instellingenDatabase, name='InstellingenDataBase'),
    path('instellingen-custom/', views.instellingenCustom, name='InstellingenCustom'),
    path('resultaat', views.resultaat, name='Resultaat'),
]
