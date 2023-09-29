from django.contrib import admin
from .models import Coupon



@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    fields = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    search_fields = ['code', 'active']
    
