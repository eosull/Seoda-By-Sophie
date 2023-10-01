# Views for basket app
from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404

from django.contrib import messages

from products.models import Product


def view_basket(request):
    # View returning user's basket
    return render(request, 'basket/basket.html')


def check_basket(comb_quan, basket_quan, request_quan, product,
                 redirect_url, request):
    # Check stock and quantity in basket
    # Returns warning if product out of stock/low in stock
    if comb_quan > product.stock_level:
        if product.stock_level - basket_quan == 0:
            messages.warning(request, f'{product.name} is out of stock')
            return redirect(redirect_url)
        else:
            messages.warning(request, f'Only {product.stock_level-basket_quan}\
                 more {product.name} remaining, please readjust quantity')
            return redirect(redirect_url)


def add_to_basket(request, product_id):
    # Add specified quantity of product to basket
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    basket_quan = 0
    comb_quan = 0

    # Using check_basket function stock level is checked
    # and if quantity desired is available it is added to
    # basket
    if product_id in list(basket.keys()):
        basket_quan = basket[product_id]
        comb_quan = quantity + basket_quan
    else:
        comb_quan = quantity

    if comb_quan > product.stock_level:
        check_basket(comb_quan, basket_quan, quantity,
                     product, redirect_url, request)
    else:
        if product_id in list(basket.keys()):
            basket[product_id] += quantity
        else:
            basket[product_id] = quantity

        messages.success(request, f'{product.name} added successfully\
                         to basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, product_id):
    # Adjust quantity of product in basket
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    basket_quan = basket[product_id]
    comb_quan = quantity + basket_quan

    # Using check_basket function stock level is checked
    # and if quantity desired is available basket is 
    # updated
    if quantity > product.stock_level:
        check_basket(comb_quan, basket_quan, quantity,
                     product, 'view_basket', request)
    else:
        if quantity > 0:
            basket[product_id] = quantity
        else:
            basket.pop(product_id)

    messages.success(request, 'Basket updated successfully')
    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, product_id):
    # Remove product from basket
    try:
        basket = request.session.get('basket', {})
        basket.pop(product_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
