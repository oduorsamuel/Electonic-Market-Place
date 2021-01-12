from django.urls import path
from .views import article_list, list_love, get_one_love, LoveData, LoveDetails, Generic

urlpatterns = [
    path('', article_list),
    path('love/', list_love),
    path('class/', LoveData.as_view()),
    path('class/<int:pk>/', LoveDetails.as_view()),
    path('generic/<int:pk>/', Generic.as_view()),
    path('generic/', Generic.as_view()),
    path('love/<int:pk>/', get_one_love)
]
