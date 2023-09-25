from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

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
    if request.method == 'POST':
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'subject': request.POST['subject'],
            'message': request.POST['message'],
        }
        contact_form = ContactForm(form_data)
        if contact_form.is_valid():
            subject = render_to_string(
                'about/contact_emails/contact_email_subject.txt',
                {'form_data': form_data})
            body = render_to_string(
                'about/contact_emails/contact_email_body.txt',
                {'form_data': form_data, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL]
            ) 
            messages.success(request, 'Message sent successfully! We will get back to you as soon as we can')
            return redirect(reverse('home'))
        else:
            messages.error(request, "Please check your form information")
    else:
        contact_form = ContactForm()
    
    template = 'about/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)
