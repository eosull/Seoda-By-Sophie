from django.shortcuts import render, redirect, reverse, HttpResponse


def view_basket(request):
    # View returning user's basket
    return render(request, 'basket/basket.html')


def add_to_basket(request, product_id):
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


def adjust_basket(request, product_id):
    # Adjust quantity of product in basket
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    print(quantity)

    if quantity > 0:
        basket[product_id] = quantity
    else:
        basket.pop(product_id)

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
