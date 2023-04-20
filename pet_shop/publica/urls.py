from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros' ),
    path('productos/', views.productos, name='productos'),
    path('blog_single/', views.blog_single, name='blog_single'),
    path('blog/', views.blog, name='blog'),
    path('contactanos/', views.contactanos, name='contactanos'),
]