
from django.shortcuts import render, redirect

from store.models.customer import Customer
from django.contrib.auth.hashers import check_password 
from django.views import View
from store.models.product import Product
from store.models.orders import Order

class Checkout(View):
    def get(self, request):
        pass

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_all_cart_product(list(cart.keys()))

        for product in products:
            order = Order(customer=Customer(id=customer),
                          product = product,
                          price = product.price,
                          address = address,
                          mobile = phone,
                          quantity = cart.get(str(product.id))
                          )    
            
        order.save()
        request.session['cart'] = {}
        return redirect('cart')
   