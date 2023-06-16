from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("login/", views.inicioSesion, name="login"),
    path("logout/", views.salir, name="exit"),
    path("crearCuenta/", views.crearCuenta, name="registro"),
    path('perfil/', views.perfil, name='perfil'),
    path('editarUsuario/', views.editarUsuario, name='editarUsuario'),
    path('editarPerfil', views.editarPerfil, name='editarPerfil'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="cuentas/password-reset.html"), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name='cuentas/password-reset-send.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='cuentas/password-reset-confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='cuentas/password-reset-completed.html'), name='password_reset_complete'),
    
]
