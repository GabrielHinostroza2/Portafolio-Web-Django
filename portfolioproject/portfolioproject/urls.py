from django.conf import settings
# Importa el objeto 'settings' de django.conf para acceder a la configuración del proyecto.

from django.conf.urls.static import static
# Importa la función 'static' de django.conf.urls.static para servir archivos estáticos y de medios en modo de depuración.

from django.contrib import admin
# Importa el módulo 'admin' de django.contrib para habilitar la administración del sitio.

from django.urls import path, include
# Importa las funciones 'path' e 'include' de django.urls para definir rutas URL y incluir otras configuraciones de URLs.

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ruta para la interfaz de administración de Django.
    # URL: 'admin/', vista: 'admin.site.urls'.

    path('', include('myportfolio.urls')),
    # Incluye las rutas URL de la aplicación 'myportfolio'.
    # URL: '', incluye: 'myportfolio.urls'.
      path('accounts/', include('django.contrib.auth.urls')),  ########Añade las vistas de autenticación de Django
      path('ckeditor', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    # Condicional para verificar si el modo de depuración está habilitado.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Si el modo de depuración está habilitado, añade las rutas para servir archivos de medios.
    # URL base: settings.MEDIA_URL, directorio raíz de documentos: settings.MEDIA_ROOT.
