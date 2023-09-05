from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    # View returning all products, search and sort queries

    products = Product.objects.all().order_by('-is_new', 'is_featured')
    query = None
    category = None
    categories = Category.objects.all()
    sel_category = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            sel_category = request.GET['category'].split(',')
            products = products.filter(category__name__in=sel_category)
            sel_category = Category.objects.filter(name__in=sel_category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messsages.error(request, "No search query entered!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    
    context = {
        'products': products,
        'search_term': query,
        'categories': categories,
        'current_category': sel_category,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    # View returning details for single product

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)