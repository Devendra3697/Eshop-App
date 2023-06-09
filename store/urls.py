from django.urls import path
from .views.login import Login, logout
from .views.signup import Signup
from .views.home import Index, store
from .views.cart import Cart
from .views.checkout import Checkout
from .views.order import OrderView
from store.middleware.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('signup', Signup.as_view(), name="signup"),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart',  Cart.as_view(), name='cart'),
    path('check-out',  Checkout.as_view(), name='checkout'),
    path('order',  auth_middleware(OrderView.as_view()), name='order')
]
