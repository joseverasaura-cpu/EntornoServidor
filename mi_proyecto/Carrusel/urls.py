from django.urls import path
from . import views

urlpatterns = [
path('', views.Carrusel)
]


from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
path('admin/', admin.site.urls),
path('', views.homepage),
# Esta línea añade automáticamente todas las urls que he vinculado en el
# punto anterior (de momento solo 1)
path('Carrusel/', include('carrusel.urls'))
]