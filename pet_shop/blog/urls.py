from django.urls import path
from . import views

urlpatterns = [
    path('blog_single/<int:blog_id>', views.BlogListViewDetail.as_view(), name='blog_single'),
    path('blog/nuevo/', views.BlogCreateView.as_view(), name='nuevoBlog'),
    path('blogs/', views.BlogListView.as_view(), name='blog'),
    path('blog/editar/<int:pk>', views.BlogUpdateView.as_view(), name='editarBlog'),
    path('blog/borrar/<int:pk>', views.BlogDelete.as_view(), name='borrarBlog')
]