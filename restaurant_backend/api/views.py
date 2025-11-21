from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    lookup_field = 'idtable'
    lookup_url_kwarg = 'idtable'


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nomplat']


class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.select_related('idplat').all().order_by('-datecom')
    serializer_class = CommandeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nomcli', 'idplat__nomplat']


class ReservViewSet(viewsets.ModelViewSet):
    queryset = Reserver.objects.all()
    serializer_class = ReservSerializer


# ------------------------------------------------------------
#  🔍 API CUSTOM : /api/clients/?date=…  ou ?start=…&end=…
# ------------------------------------------------------------
@api_view(['GET'])
def clients_history(request):
    date = request.GET.get("date")
    start = request.GET.get("start")
    end = request.GET.get("end")

    qs = Commande.objects.select_related("idplat")

    if date:
        qs = qs.filter(datecom__date=date)

    if start and end:
        qs = qs.filter(datecom__date__range=[start, end])

    return Response(CommandeSerializer(qs, many=True).data)
