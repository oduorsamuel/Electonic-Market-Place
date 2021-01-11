from django.urls import path
from .views import article_list, list_love , get_one_love

urlpatterns = [
    path('', article_list),
    path('/love', list_love),
    path('/love/<int:pk>/', get_one_love)
]
