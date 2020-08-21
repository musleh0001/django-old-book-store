from django.shortcuts import render
from dashboard.models import Book
from .models import Cart, OrderSingleProduct, BillingAddress
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateBillingAddress

@login_required()
def add_to_cart(request,id):    
	#add to cart 
	if request.user.is_authenticated:
		
		cart = Cart.objects.filter(user=request.user, ordered=False)

		if cart.exists():
			order_item = cart[0].products.filter(user=request.user, ordered=False, product_id = id)
			if order_item.exists():
				order_item=order_item[0]
				order_item.quantity+=1
				order_item.save()
				messages.info(request,"Product Added To Cart")
				return redirect('order:Cart')
			else:
				order_item = cart[0].products.create(user=request.user, ordered=False, product_id = id)
				order_item.save()
				cart[0].save()
				messages.info(request,"Product Added To Cart")
				return redirect('order:Cart')	
		else:
			cart = Cart.objects.create(user=request.user, ordered=False)
			cart.save()
			single_item = OrderSingleProduct.objects.create (user=request.user, ordered=False, product_id = id)
			cart.products.add(single_item)
			cart.save()
			messages.info(request,"Product Added To Cart")
			return redirect('order:Cart')
	else:
		messages.warning(request,"You need to login")
		return redirect('/')


@login_required()
def remove_from_cart(request,id):    
	#add to cart 
	if request.user.is_authenticated:
		
		cart = Cart.objects.filter(user=request.user, ordered=False)

		if cart.exists():
			cart = cart[0]	#catch the very first order over this condition
			order_item = cart.products.filter(user=request.user, ordered=False, product_id = id)
			if order_item.exists():
				order_item=order_item[0]
				if order_item.quantity>1:
					order_item.quantity-=1
					order_item.save()
					cart.save()
					messages.info(request,"Removed a quantity")
				else:
					messages.info(request,"Removed a Book from cart")
					cart.products.remove()
					order_item.delete()

				return redirect('order:Cart')

			else:
				messages.info(request,"This Product is not in your cart")
				return redirect('order:Cart')	
		else:
			messages.info(request,"You don't have an active cart")
			return redirect('/')
	else:
		messages.warning(request,"You need to login")
		return redirect('/')

@login_required()
def delete_from_cart(request,id):    
	#add to cart 
	if request.user.is_authenticated:
		
		cart = Cart.objects.filter(user=request.user, ordered=False)

		if cart.exists():
			cart = cart[0]
			order_item = cart.products.filter(user=request.user, ordered=False, product_id = id)
			if order_item.exists():
				order_item=order_item[0]
				cart.products.remove()
				order_item.delete()
				cart.save()

				messages.info(request,"Deleted a Book from cart")
				return redirect('order:Cart')

			else:
				messages.info(request,"This Product is not in your cart")
				return redirect('order:Cart')	
		else:
			messages.info(request,"You don't have an active cart")
			return redirect('/')
	else:
		messages.warning(request,"You need to login")
		return redirect('/')

class Checkout(LoginRequiredMixin, View):
	
	def get(self, request, *args, **kwargs):

		if request.user.is_authenticated:
			previous= BillingAddress.objects.filter(user=request.user)
			
			if previous.exists():
				previous = previous[0]
				form = CreateBillingAddress(instance = previous)
			else:
				form = CreateBillingAddress

			context= {'form':form,}
			return render(request, 'order/checkout.html', context)
		
		messages.warning(request,"Please login and try again")	
		return redirect('/')
	
	def post(self, request, *args, **kwargs):
		
		if request.user.is_authenticated:
			previous= BillingAddress.objects.filter(user=request.user)
			if previous.exists():
				previous = previous[0]
				form = CreateBillingAddress(request.POST,instance = previous)
			else:
				form = CreateBillingAddress(request.POST)
				
			if form.is_valid():
				form.instance.user = request.user
				form.save()
				messages.warning(request,"Billing Address is changed")
				return redirect('order:Checkout')

			messages.warning(request,"Request is not valid, try again")	
			return redirect('order:Checkout')

		messages.warning(request,"Please login and try again")	
		return redirect('/')

class CartView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):

		cart = Cart.objects.filter(user = request.user, ordered=False)

		if cart.exists():
			cart = cart[0]
		else:
			cart = None
		context = {'cart':cart, }
	
		return render(request, 'order/cart.html', context)