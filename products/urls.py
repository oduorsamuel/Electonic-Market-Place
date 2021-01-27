from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shop', views.shop),
    path('blog', views.blog),
    path('about', views.about),
    path('contact', views.contact),
    path('cart', views.cart),
    path('checkout', views.checkout)
]
