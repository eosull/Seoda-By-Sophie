

def basket_contents(request):

    basket_items = []
    total = 0 
    product_count = 0
    delivery = settings.STANDARD_DELIVERY

    grand_total = total + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
    }

    return context
