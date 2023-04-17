from django.shortcuts import render
from .models import Product


def product(request):
    return render(request,"product/product.html")

def products(request):
    pro = Product.objects.all()
    x =  {"product" : pro}
    return render(request,"product/products.html", x)