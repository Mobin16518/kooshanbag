from django.contrib import admin
from django.urls import path , include
from . import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('product/', include(('products.urls', 'product'), namespace='products')),
    path('account/', include(('account.urls', 'account'), namespace='account')),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
