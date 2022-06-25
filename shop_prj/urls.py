from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('customers/', include('customers.urls')),
    path('', RedirectView.as_view(url=reverse_lazy('home-page'), permanent=False)),
    # path(r'^cart/', include('cart.urls', namespace='cart')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
