from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def blog(request):
    titulo = 'Blog de Novedades'
    contexto = { 'titulo' : titulo}
    return render(request, 'blog/blog.html', contexto)

def blog_single(request):
    titulo = 'Blog de Novedades'
    contexto = { 'titulo' : titulo}
    return render(request, 'blog/blog-single.html', contexto)