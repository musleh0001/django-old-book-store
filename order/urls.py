from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
	path('add-to-cart/<int:id>/',views.add_to_cart, name='AddToCart'),
	path('remove-cart/<int:id>/',views.remove_from_cart, name='RemoveCart'),
	path('delete-cart/<int:id>/',views.delete_from_cart, name='DeleteCart'),
	path('cart/',views.CartView.as_view(), name = 'Cart'),
	path('checkout/',views.Checkout.as_view(), name = 'Checkout'),
]
