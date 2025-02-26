from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import (CakeViewSet, ModificationsViewSet, VariablesOfModificationViewSet, OrderViewSet, CustomUserViewSet)

router = routers.DefaultRouter()
router.register('cakes', CakeViewSet)
router.register('modifications', ModificationsViewSet)
router.register('variables', VariablesOfModificationViewSet)
router.register('orders', OrderViewSet)
router.register('customusers', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
