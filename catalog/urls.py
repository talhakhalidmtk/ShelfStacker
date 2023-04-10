from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='books')
router.register(r'publishers', views.PublisherViewSet, basename='publishers')
router.register(r'book_contributors', views.BookContributorViewSet, basename='book_contributors')
router.register(r'racks', views.RackViewSet, basename='racks')

urlpatterns = [
    path('', include((router.urls, 'api'))),
]
