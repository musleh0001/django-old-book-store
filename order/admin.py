from django.contrib import admin
from .models import OrderSingleProduct, Order, BillingAddress


admin.site.register(OrderSingleProduct)
admin.site.register(Order)
admin.site.register(BillingAddress)
