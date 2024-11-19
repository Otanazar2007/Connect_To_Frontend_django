from django.shortcuts import render

from main.models import Product, CategoryProduct, UserCart


# Create your views here.
def home_page(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'home.html', context)

def categories(request):
    categories = CategoryProduct.objects.all()
    context = {
        'categories': categories
    }
    return render(request, "categories.html", context)

def user_carts(request):
    user_cart = UserCart.objects.all()
    context = {
        'user_cart':user_cart
    }
    return render(request, 'user_cart.html', context)