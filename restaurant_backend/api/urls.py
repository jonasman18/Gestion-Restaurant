from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TableViewSet,
    MenuViewSet,
    CommandeViewSet,
    ReservViewSet
)

router = DefaultRouter()
router.register('tables', TableViewSet)
router.register('menus', MenuViewSet)
router.register('commandes', CommandeViewSet)
router.register('reservations', ReservViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
