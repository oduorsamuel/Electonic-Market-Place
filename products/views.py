from django.http import HttpResponse
from .models import Products
from django.shortcuts import render


def index(request):
    products = Products.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New product')

# Create your views here.
