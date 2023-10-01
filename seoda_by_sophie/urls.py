# URLS for site apps
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static

handler404 = 'seoda_by_sophie.views.error404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('about/', include('about.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
