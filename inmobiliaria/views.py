from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Inmueble



def index(request):
    # Obtén todos los inmuebles desde la base de datos
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmobiliaria/index.html' , {'inmuebles': inmuebles})

def inmueble_detail(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, pk=inmueble_id)
    return render(request, 'inmobiliaria/inmuebles_detail.html', {'inmueble': inmueble})

def about(request):
    return render (request, 'inmobiliaria/about.html')

def blog_details(request):
    return render (request, 'inmobiliaria/blog-details.html')

def blog(request):
    return render (request, 'inmobiliaria/blog.html')

def contact(request):
    return render (request, 'inmobiliaria/contact.html')

def portfolio(request):
    return render (request, 'inmobiliaria/portfolio.html')

def services(request):
    return render (request, 'inmobiliaria/services.html')