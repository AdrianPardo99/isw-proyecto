"""Proyecto_Arbolado URL Configuration """

from django.contrib import admin
from django.urls import path, re_path, include
# Importamos los settings
from django.conf import settings
# Importamos los archivos estáticos
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.arbolado.urls')),
    re_path('', include('applications.solicitudes.urls')),
    # Ckeditor urls
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
