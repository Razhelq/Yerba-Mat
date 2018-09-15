from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Product, Client, Basket, InsideBasket, Category, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'amount', 'category', 'picture']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    last_display = ['name', 'description']


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    last_display = ['person', 'product', 'total_price']


@admin.register(InsideBasket)
class InsideBasket(admin.ModelAdmin):
    last_display = ['basket', 'product', 'items']


@admin.register(Order)
class Order(admin.ModelAdmin):
    last_display = ['basket', 'person', 'creation_date', 'paid', 'sent', 'name', 'last_name', 'street', 'post', 'city', 'phone']


class ClientInline(admin.StackedInline):
    model = Client
    can_delete = False
    verbose_name_plural = 'client'


class UserAdmin(BaseUserAdmin):
    inlines = (ClientInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

