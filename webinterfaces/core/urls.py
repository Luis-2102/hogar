from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('Nosotros/', views.about, name='Nosotros'),
    path('Asesor/', views.agent_single, name='Asesor'),
    path('Asesores/', views.agent_grid, name='Asesores'),
    path('Novedades/', views.blog_grid, name='Novedades'),
    path('blog-single/', views.blog_single, name='blog-single'),
    path('Contacto/', views.contact, name='Contacto'),
    path('Propiedades/', views.property_grid, name='Propiedades'),
    path('Propiedad/', views.property_single, name='Propiedad'),
]
