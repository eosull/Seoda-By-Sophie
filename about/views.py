from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from .forms import ContactForm
from .models import Faq, InfoCategory


def about(request):
    # View returning index page
    return render(request, 'about/about.html')


def faqs(request):
    # View returning FAQ page
    categories = InfoCategory.objects.all()
    faq = Faq.objects.all()
    context = {
        'categories': categories,
        'faq': faq,
    }

    return render(request, 'about/faq.html', context)


def contact(request):
    # View to handle contact form submission
    form_data = {
        'name': request.POST['name'],
        'email': request.POST['email'],
        'subject': request.POST['subject'],
        'message': request.POST['message'],
    }
    if request.method == 'POST':
        contact_form = ContactForm(form_data)
    if contact_form.is_valid():
        # SEND EMAIL
        messages.success(request, 'Message sent successfully! We will get back to you as soon as we can')
        return redirect(reverse('home'))
    else:
        messages.error(request, "Please check your form information")
    
    return render(request, 'about/contact.html')
