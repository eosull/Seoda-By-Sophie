from django.shortcuts import render
from .models import Product


def all_products(request):
    # View returning all products, search and sort queries

    products = Product.objects.all().order_by('-is_new', 'is_featured')

    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)