from django.urls import path
from . import views

urlpatterns = [
    path('blog_single/<int:blog_id>', views.BlogListViewDetail.as_view(), name='blog_single'),
    #path('blog/', views.blog, name='blog'),
    path('blogs/', views.BlogListView.as_view(), name='blog'),
]