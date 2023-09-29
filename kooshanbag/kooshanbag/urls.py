from django.contrib import admin
from django.urls import path , include
from . import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include("home.urls")),
    path('admin/', admin.site.urls),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('account/', include(('account.urls', 'account'), namespace='account')),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
    path('coupons/', include(('coupons.urls', 'coupons'), namespace='coupons')),
    path('product/', include(('products.urls', 'product'), namespace='products')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
