from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    # View returning all products, search and sort queries

    products = Product.objects.all().order_by('-is_new', 'is_featured')

    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    # View returning details for single product

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)