"""
User App URLs
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, APIKeyViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')
router.register(r'api-keys', APIKeyViewSet, basename='apikey')

urlpatterns = router.urls

