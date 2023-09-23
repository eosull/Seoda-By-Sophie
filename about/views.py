from django.shortcuts import render
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
