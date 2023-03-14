
from django.shortcuts import render, redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View

# Create your views here.
class Index(View):

    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')
    
    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart= request.session.get('cart')
        
        if cart:
            quentity = cart.get(product)
            if quentity:
                if remove:
                    if quentity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quentity - 1    
                else:
                    cart[product] = quentity + 1    
            else:
                cart[product] = 1    
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart     
        return redirect('homepage')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:  
        products = Product.get_all_product_categoryId(categoryID)
    else:
        products = Product.get_all_product();

    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)


