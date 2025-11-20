from rest_framework import viewsets, filters
from restaurant.models import Table, Menu, Commande, Reserver
from .serializers import (
    TableSerializer,
    MenuSerializer,
    CommandeSerializer,
    ReservSerializer
)


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nomplat']


class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nomcli']


class ReservViewSet(viewsets.ModelViewSet):
    queryset = Reserver.objects.all()
    serializer_class = ReservSerializer
