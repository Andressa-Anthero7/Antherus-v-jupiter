"""antherus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landingpage.urls')),
    path('dashboard/caixa-leads/', include('landingpage.urls')),
    path('leads/<int:pk>/', include('landingpage.urls')),
    path('status/<int:pk>/', include('landingpage.urls')),
    path('area-adm/', include('landingpage.urls')),
    path('cadastro-clientes/', include('landingpage.urls')),
    path('cliente/<int:pk>/', include('landingpage.urls')),
    path('lista-clientes/', include('landingpage.urls')),
    path('editar-cliente/<int:pk>/', include('landingpage.urls')),
    path('deletar-cliente/<int:pk>/', include('landingpage.urls')),
    path('cliente-deletado/', include('landingpage.urls')),
    path('cadastro-produtos/', include('landingpage.urls')),
    path('lista-produtos/', include('landingpage.urls')),
    path('editar-listagem-produtos/<int:pk>/', include('landingpage.urls')),
    path('deletar-produtos/<int:pk>/', include('landingpage.urls'))
]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)