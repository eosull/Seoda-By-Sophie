# Contexts to calculate totals in basket
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    # Getting the basket
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    # Looping through contents of session basket and adding to
    # basket_items variable for use in the template
    for product_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=product_id)
        if product.on_sale:
            total += quantity * product.sale_price
        else:
            total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
        })

    # Adding delivery cost if products in basket
    if product_count:
        delivery = settings.STANDARD_DELIVERY
    else:
        delivery = 0
        
    grand_total = total + Decimal(delivery)

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
