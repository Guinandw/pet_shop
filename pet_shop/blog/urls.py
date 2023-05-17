from django.urls import path
from . import views

urlpatterns = [
    path('blog_single/', views.blog_single, name='blog_single'),
    path('blog/', views.blog, name='blog'),
]