from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm


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


@login_required
def add_product(request):
    # Add a product to the store
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the site admin can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            # messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        # else:
        #     messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    # Edit a product
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the site admin can do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid:
            form.save()
            # messages.success(request, f'Successfully edited {product.name}')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product, please check form for errors')
    form = ProductForm(instance=product)
    # messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def confirm_delete(request, product_id):
    # Confirm delete
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the site admin can do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    template = 'products/delete_product.html'
    context = {
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    # Delete a product
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the site admin can do that')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    # messages.success(request, 'Product deleted')
    return redirect(reverse('products'))
