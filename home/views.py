from django.shortcuts import render


def index(request):
    # View returning index page
    return render(request, 'home/index.html')
