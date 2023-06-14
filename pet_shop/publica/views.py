from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.conf import settings


from publica.forms import ContactanosForms

from django.contrib import messages

# Create your views here.
def inicio(request):
    titulo = 'Pet Shop'
    contexto = { 'titulo' : titulo}
   
    return render(request, 'publica/index.html', contexto)

def nosotros(request):
    titulo = 'Nosotros'
    contexto = { 'titulo' : titulo}
    return render(request, 'publica/about.html', contexto)



def contactanos(request):
    titulo = 'Contactanos'
    if(request.method=='POST'):
        contacto_form = ContactanosForms(request.POST)
        
        if(contacto_form.is_valid()):
            print(request.POST['mensaje'])
            print(contacto_form.cleaned_data['mensaje'])
            messages.success(request,'Hemos recibido tus datos')
            nombre = contacto_form.cleaned_data['nombre']
            toemail= contacto_form.cleaned_data['email']
            asunto = nombre +'Hemos recibido tu peticion sobre: '+request.POST['asunto']
            mensaje = contacto_form.cleaned_data['mensaje']
            mensaje_html=f"""
                <p>De: {contacto_form.cleaned_data['nombre']} <a href="mailto:{contacto_form.cleaned_data['email']}">{contacto_form.cleaned_data['email']}</a></p>
                <p>Asunto:  {contacto_form.cleaned_data['asunto']}</p>
                <p>Mensaje: {contacto_form.cleaned_data['mensaje']}</p>
            """
            
            send_mail(subject=asunto,
                      message=mensaje,
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list= [toemail], fail_silently=False,
                      html_message=mensaje_html
                      ) 
            #limpiando el formulario
            #contacto_form = ContactanosForms()
        else:  
            messages.warning(request, 'Por favor verificar los datos')
    else:
        contacto_form= ContactanosForms()
            
    
    
    contexto = { 
                'titulo' : titulo,
                'contacto_form': contacto_form
                }
    return render(request, 'publica/contacto.html', contexto)



""" def producto_simple(request):
    titulo = 'Producto'
    contexto = { 'titulo' : titulo}
    return render(request, 'publica/product-single.html', contexto)
 """
