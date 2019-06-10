"""datasad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from comum import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='exibir_index'),
    path('login/', views.exibir_login, name='exibir_login'),
    path('usuario/novo/', views.exibir_cadastro_usuario, name='exibir_cadastro_usuario'),
    path('home/', views.exibir_home, name='exibir_home'),
    path('questionario/id', views.exibir_questionario_detail, name='exibir_questionario_detail'),
]
