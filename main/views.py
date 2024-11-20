from django.shortcuts import render

from main.models import Product, CategoryProduct, UserCart


# Create your views here.
def home_page(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'index.html', context)

def categories_page(request, pk):
    all_categories = CategoryProduct.objects.all()
    categories = CategoryProduct.objects.get(id=pk)
    products = Product.objects.filter(product_category = categories).all()
    context = {
        'all_categories':all_categories,
        'categories': categories,
        'products': products
    }
    return render(request, "categories.html", context)

def user_carts(request):
    user_cart = UserCart.objects.all()
    context = {
        'user_cart':user_cart
    }
    return render(request, 'user_cart.html', context)