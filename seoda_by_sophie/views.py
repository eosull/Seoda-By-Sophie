from django.shortcuts import render


def error404(request, exception):
    # View returning index page
    return render(request, '404.html', status=404)

