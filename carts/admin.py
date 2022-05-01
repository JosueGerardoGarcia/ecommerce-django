from django.contrib import admin
from .models import Cart, Cartitem
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')

class CartitemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')


admin.site.register(Cart, CartAdmin)
admin.site.register(Cartitem, CartitemAdmin)
