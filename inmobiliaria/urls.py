from django.urls import path, include
from . import views

app_name = 'inmobiliaria' 

urlpatterns = [
    path('', views.index, name='index'),
    path('inmuebles/<int:inmueble_id>/', views.inmueble_detail, name='inmueble_detail'),

    path('about/', views.about, name='about'),
    path('blog-details/', views.blog_details, name='blog-details'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
]