"""ecomfree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views
from store import views as views_store
from usuarios import views as views_usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_store.home, name='inicio'),
    path('buscar/', views_store.buscarSinTermino),
    path('buscar/<str:termino>', views_store.buscar),
    path('categoria/<str:cat>', views_store.buscar_categoria),
    path('productos/<int:id_producto>', views_store.detalle_producto),
    path('registro', views_usuarios.registar, name='registro'),
    path('acceder', auth_views.LoginView.as_view(), name='login'),
    path('salir', auth_views.LogoutView.as_view(), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
