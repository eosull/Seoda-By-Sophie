from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact/', views.contact, name='contact'),
]
