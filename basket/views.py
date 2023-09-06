from django.shortcuts import render


def view_basket(request):
    # View returning user's basket
    return render(request, 'basket/basket.html')
