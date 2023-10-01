# Urls for about app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('faqs/', views.faqs, name='faqs'),
    path('add_faq/', views.add_faq, name='add_faq'),
    path('edit/<int:faq_id>/', views.edit_faq, name='edit_faq'),
    path('confirm_faq_delete/<int:faq_id>', views.confirm_faq_delete,
         name='confirm_faq_delete'),
    path('delete/<int:faq_id>/', views.delete_faq, name='delete_faq'),
    path('contact/', views.contact, name='contact'),
]
