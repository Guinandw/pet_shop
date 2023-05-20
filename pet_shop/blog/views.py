from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Blog
# Create your views here.


""" def blog(request):
    titulo = 'Blog de Novedades'
    contexto = { 'titulo' : titulo}
    return render(request, 'blog/blog.html', contexto) """

def blog_single(request):
    titulo = 'Blog de Novedades'
    contexto = { 'titulo' : titulo}
    return render(request, 'blog/blog-single.html', contexto)
    
'''
        IMPLEMENTACION DEL BLOG CON VISTAS BASADAS EN CLASES
'''

class BlogListView(ListView):
    model = Blog
    
    template_name = 'blog/blog.html'
    ordering = ['fecha']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        context['titulo'] = 'Blog de Novedades'
        return context

class BlogListViewDetail(ListView):
    model = Blog
    template_name = 'blog/blog-single.html'
    ordering = ['fecha']
    
    def get_queryset(self):
        self.blog = get_object_or_404(Blog, pk=self.kwargs["blog_id"])
        return self.blog
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        context['blog'] = self.blog
        context['titulo'] = 'Blog de Novedades'
        return context    