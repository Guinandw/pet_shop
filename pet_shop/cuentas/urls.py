from django.urls import path
from . import views
urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="exit"),
    path("crearCuenta/", views.crearCuenta, name="registro"),
]
