from django.contrib import admin
from django.urls import path, include
from pdf.views import facture_pdf
from stats.views import recette_totale, recettes_6_mois

urlpatterns = [
    path('admin/', admin.site.urls),

    # API REST
    path('api/', include('api.urls')),

    # Factures PDF
    path('pdf/<str:idcom>/', facture_pdf),

    # Statistiques
    path('stats/total/', recette_totale),
    path('stats/6mois/', recettes_6_mois),
]
