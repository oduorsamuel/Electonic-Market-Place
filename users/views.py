from django.shortcuts import render
from django.http import HttpResponse
from .models import UserModel


# Create your views here.

def index(request):
    users = UserModel.objects.all()
    return render(request, 'index2.html', {'users': users})
