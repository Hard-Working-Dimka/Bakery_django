from rest_framework import viewsets

from .serializers import (CakeSerializer, ModificationsSerializer, VariablesOfModificationSerializer, OrderSerializer,
                          CustomUserSerializer)
from cakes.models import Cake, CustomUser, Modifications, VariablesOfModification, Order


class CakeViewSet(viewsets.ModelViewSet):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
