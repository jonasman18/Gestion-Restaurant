from rest_framework import serializers
from restaurant.models import Table, Menu, Commande, Reserver


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class CommandeSerializer(serializers.ModelSerializer):
    # Champ calculé automatiquement
    total = serializers.IntegerField(read_only=True)

    class Meta:
        model = Commande
        fields = '__all__'


class ReservSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserver      # 🔥 Correction ici
        fields = '__all__'
