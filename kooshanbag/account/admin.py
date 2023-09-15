from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Otp




@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "phone", "f_name", "l_name", "is_admin"]
    search_fields = ["email", "phone"]
    ordering = ["email", "phone"]
    list_filter = ["is_admin"]
    filter_horizontal = []



admin.site.unregister(Group)

