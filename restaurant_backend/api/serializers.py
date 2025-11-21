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
    nomplat = serializers.SerializerMethodField()
    pu = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    

    class Meta:
        model = Commande
        fields = '__all__'

    def get_nomplat(self, obj):
        return obj.idplat.nomplat

    def get_pu(self, obj):
        return obj.idplat.pu

    def get_total(self, obj):
        return obj.quantite * obj.idplat.pu


class ReservSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserver
        fields = '__all__'

    def validate(self, data):
        idtable = data.get('idtable')
        date_reserve = data.get('date_reserve')
        idreserv = self.instance.idreserv if self.instance else None

        exists = Reserver.objects.filter(
            idtable=idtable,
            date_reserve=date_reserve
        ).exclude(idreserv=idreserv).exists()

        if exists:
            raise serializers.ValidationError(
                "Cette table est déjà réservée à ce moment."
            )

        return data
