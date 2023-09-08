from django.shortcuts import render, redirect


def view_basket(request):
    # View returning user's basket
    return render(request, 'basket/basket.html')


def add_to_bag(request, product_id):
    # Add specified quantity of product to basket
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if product_id in list(basket.keys()):
        basket[product_id] += quantity
    else:
        basket[product_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)