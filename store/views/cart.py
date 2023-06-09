
from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_all_cart_product(ids)
        
        return render(request, 'cart.html', {'products': products})         

   