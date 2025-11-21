from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TableViewSet,
    MenuViewSet,
    CommandeViewSet,
    ReservViewSet,
    clients_history
)

router = DefaultRouter()
router.register('tables', TableViewSet, basename='tables')
router.register('menus', MenuViewSet)
router.register('commandes', CommandeViewSet)
router.register('reservations', ReservViewSet)


urlpatterns = [
    path('', include(router.urls)),

    # 🔍 Historique des clients
    path('clients/', clients_history),
]
