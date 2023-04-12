from django.urls import path, include
from rest_framework import routers
from .views import LendViewSet

router = routers.DefaultRouter()
router.register('', LendViewSet, basename='lend')

urlpatterns = [
    path('', include(router.urls)),
]
