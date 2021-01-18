from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import article_list, list_love, get_one_love, LoveData, LoveDetails, Generic, LoveViewSet

router = DefaultRouter()
router.register('love', LoveViewSet, basename='love')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('', article_list),
    path('love/', list_love),
    path('class/', LoveData.as_view()),
    path('class/<int:pk>/', LoveDetails.as_view()),
    path('generic/<int:pk>/', Generic.as_view()),
    path('generic/', Generic.as_view()),
    path('love/<int:pk>/', get_one_love)
]
