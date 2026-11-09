from django.urls import path
from . import views
app_name = "enraya"
urlpatterns = [
path('', views.enraya, name='homepage')
]