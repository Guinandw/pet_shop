from django.urls import path
from . import views
urlpatterns = [
    path("login/", views.inicioSesion, name="login"),
    path("logout/", views.salir, name="exit"),
    path("crearCuenta/", views.crearCuenta, name="registro"),
    path('perfil', views.perfil, name='perfil'),
]
