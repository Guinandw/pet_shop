from typing import Any, Dict, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, response
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Blog
from .forms import BlogCrearForm
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        buscador = self.request.GET.get('buscarBlog')
        if buscador:
            context['blogs'] = Blog.objects.filter(titulo__icontains=buscador)
        else:
            context['blogs'] = Blog.objects.all().order_by('-fecha')
        context['titulo'] = 'Blog de Novedades'
        return context
    
      
 
class BlogListViewDetail(ListView):
    model = Blog
    template_name = 'blog/blog-single.html'
    
    def get_queryset(self):
        self.blog = get_object_or_404(Blog, pk=self.kwargs["blog_id"])
        return self.blog
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all().order_by('-fecha')[0:3]
        context['blog'] = self.blog
        context['titulo'] = 'Blog de Novedades'
        return context    




class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogCrearForm
    template_name = 'blog/crearBlog.html'
    success_url = reverse_lazy('blog')
    
    
class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    template_name = 'blog/editarBlog.html'
    success_url = reverse_lazy('blog')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        context['blog'] = Blog.objects.filter(pk=pk)
        context['titulo'] = 'Blog de Novedades - Editar'
        return context
    
    
    
class BlogDelete(DeleteView):
    model = Blog
    template_name ='blog/borrarBlog.html'
    success_url = reverse_lazy('blog')
    
    def get_object(self, queryset= None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        blog = get_object_or_404(Blog, pk=pk)
        return blog