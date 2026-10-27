from django.urls import path
from . import views
app_name = "calendario"

urlpatterns = [
    #Con esta línea creamos una url genérica que va a hacer coincidencia con todas las URLs que cumplan esa forma. Por seguridad y buen funcionamiento, cuanto más genérica sea el patrón más cerca del fondo de la lista urlpatterns debería encontrarse.
    path('<str:fecha>', views.calendario, name='calendario'),
]