from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),  # Existing route

    path('contact/', views.contact, name='contact'),
    path('r404/', views.r404, name='r404'),
    path('faq/', views.faq, name='faq'),
    path('feature/', views.feature, name='feature'),
    path('offer/', views.offer, name='offer'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('blog/', views.blog, name='blog'),
]
