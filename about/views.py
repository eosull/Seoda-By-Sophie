from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.paginator import Paginator
from django.core.mail import send_mail

from django.template.loader import render_to_string
from django.conf import settings

from .forms import ContactForm, FaqForm
from .models import Faq, InfoCategory, Testimonial


def about(request):
    # View returning index page
    testimonials = Testimonial.objects.all()
    paginator = Paginator(testimonials, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'about/about.html', context)


def faqs(request):
    # View returning FAQ page
    categories = InfoCategory.objects.all()
    faq = Faq.objects.all()
    context = {
        'categories': categories,
        'faq': faq,
    }

    return render(request, 'about/faq.html', context)

@login_required
def add_faq(request):
    # Add an faq
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the site admin can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES)
        if form.is_valid():
            faq = form.save()
            messages.success(request, 'Successfully added Faq!')
            return redirect(reverse('faqs'))
        else:
            messages.error(request, 'Failed to add faq. Please ensure the form is valid.')
    else:
        form = FaqForm()

    template = 'about/add_faq.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_faq(request, faq_id):
    # Edit an faq
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the site admin can do that')
        return redirect(reverse('home'))

    faq = get_object_or_404(Faq, pk=faq_id)
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES, instance=faq)
        if form.is_valid:
            form.save()
            messages.success(request, f'Successfully edited question {faq.question}')
            return redirect(reverse('faqs'))
        else:
            messages.error(request, 'Failed to update faq, please check form for errors')
    form = FaqForm(instance=faq)
    messages.info(request, f'You are editing question {faq.question}')

    template = 'about/edit_faq.html'
    context = {
        'form': form,
        'faq': faq,
    }

    return render(request, template, context)


@login_required
def confirm_faq_delete(request, faq_id):
    # Confirm delete
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the site admin can do that')
        return redirect(reverse('home'))

    faq = get_object_or_404(Faq, pk=faq_id)
    template = 'about/delete_faq.html'
    context = {
        'faq': faq,
    }

    return render(request, template, context)


@login_required
def delete_faq(request, faq_id):
    # Delete an Faq
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the site admin can do that')
        return redirect(reverse('home'))
        
    faq = get_object_or_404(Faq, pk=faq_id)
    faq.delete()
    messages.success(request, 'Faq deleted')
    return redirect(reverse('faqs'))


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
