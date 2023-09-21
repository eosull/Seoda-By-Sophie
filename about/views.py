from django.shortcuts import render


def about(request):
    # View returning index page
    return render(request, 'about/about.html')

