from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Product, Client

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'amount', 'category', 'picture']


class ClientInline(admin.StackedInline):
    model = Client
    can_delete = False
    verbose_name_plural = 'client'


class UserAdmin(BaseUserAdmin):
    inlines = (ClientInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

