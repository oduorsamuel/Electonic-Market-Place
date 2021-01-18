from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import article_list, list_love, get_one_love, LoveData, LoveDetails,\
    Generic, LoveViewSet,GenericViewSet , ModalViewSet

router = DefaultRouter()
router2 = DefaultRouter()
router3 = DefaultRouter()
router.register('love', LoveViewSet, basename='love')
router2.register('generic', GenericViewSet, basename='generic')
router3.register('home', ModalViewSet, basename='home')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('view/', include(router2.urls)),
    path('view/<int:pk>/', include(router2.urls)),
    path('modal/', include(router3.urls)),
    path('modal/<int:pk>/', include(router3.urls)),
    path('', article_list),
    path('love/', list_love),
    path('class/', LoveData.as_view()),
    path('class/<int:pk>/', LoveDetails.as_view()),
    path('generic/<int:pk>/', Generic.as_view()),
    path('generic/', Generic.as_view()),
    path('love/<int:pk>/', get_one_love)
]
