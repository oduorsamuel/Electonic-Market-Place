from django.http import HttpResponse
from .models import Products
from django.shortcuts import render


def index(request):
    products = Products.objects.all()
    print(products)
    return render(request, 'index.html', {'products': products})


def shop(request):
    return render(request, 'shop.html')


def blog(request):
    return render(request, 'blog.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')

# Create your views here.
