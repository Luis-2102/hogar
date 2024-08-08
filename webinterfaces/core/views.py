from django.views.generic.base import TemplateView
from django.shortcuts import render

class home(TemplateView):
    def get(self, request):
        return render(request, 'index.html')

def about(request):
    return render(request, 'Nosotros.html')

def agent_single(request):
    return render(request, 'Asesor.html')

def agent_grid(request):
    return render(request, 'Asesores.html')

def blog_grid(request):
    return render(request, 'Novedades.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def contact(request):
    return render(request, 'Contacto.html')

def property_grid(request):
    return render(request, 'Propiedades.html')

def property_single(request):
    return render(request, 'Propiedad.html')
