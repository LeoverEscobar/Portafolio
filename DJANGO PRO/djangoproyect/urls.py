from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls

from .views import inicio, portafolio, exit  # Asegúrate de importar tus vistas correctamente
from Aplicaciones.tictactoe.views import display_board, make_move  # Importa las vistas de tictactoe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name="inicio"),
    path('portafolio/', portafolio, name="portafolio"),
    path('exit/', exit, name="exit"),
    path("accounts/", include('django.contrib.auth.urls')),
    path("", include('Aplicaciones.portafolio.urls')),
    path("", include('Aplicaciones.contacto.urls')),
    path("", include('Aplicaciones.ubicaciones.urls')),
    path("api/v1/", include('Aplicaciones.directorio.urls')),
    path("docs/", include_docs_urls(title='Api Documentation')),
    path('tictactoe/', include('Aplicaciones.tictactoe.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]