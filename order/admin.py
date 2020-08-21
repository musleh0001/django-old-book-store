from django.contrib import admin
from .models import OrderSingleProduct, Cart, BillingAddress


admin.site.register(OrderSingleProduct)
admin.site.register(Cart)
admin.site.register(BillingAddress)
