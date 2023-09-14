from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'There is nothing currently in your basket')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NajcEKw17anif8ojAMWNgKhBfgeov6CF4MT4Zp4pS9TU2flkWcoxirIHzhBByO1tB2jSKhRPN24ClgHRZy8fXpS00G50viayD',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
