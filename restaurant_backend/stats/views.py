from django.db.models import Sum, F
from django.db.models.functions import TruncMonth
from restaurant.models import Commande
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def recette_totale(request):
    """
    Retourne la somme totale de toutes les recettes du restaurant.
    """
    total = Commande.objects.aggregate(
        total=Sum(F('quantite') * F('idplat__pu'))
    )
    return Response(total)


@api_view(['GET'])
def recettes_6_mois(request):
    """
    Retourne les recettes des 6 derniers mois pour l'histogramme.
    """
    data = (
        Commande.objects
        .annotate(month=TruncMonth('datecom'))
        .values('month')
        .annotate(total=Sum(F('quantite') * F('idplat__pu')))
        .order_by('-month')[:6]
    )

    return Response(data)
