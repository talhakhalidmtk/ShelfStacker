from django.urls import path, include
from rest_framework import routers
from .views import MembershipViewSet

router = routers.DefaultRouter()
router.register('', MembershipViewSet, basename='memberships')

urlpatterns = [
    path('', include(router.urls)),
]
