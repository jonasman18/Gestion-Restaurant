from django.db import models


# ============================
# 🟦 TABLE
# ============================
class Table(models.Model):
    idtable = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=50)
    occupation = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.idtable} - {self.designation}"


# ============================
# 🟦 MENU
# ============================
class Menu(models.Model):
    idplat = models.AutoField(primary_key=True)
    nomplat = models.CharField(max_length=100)
    pu = models.IntegerField()

    def __str__(self):
        return f"{self.nomplat} ({self.pu} Ar)"


# ============================
# 🟦 COMMANDE
# ============================
class Commande(models.Model):
    TYPE_CHOICES = [
        ('TABLE', 'Sur table'),
        ('EMPORTER', 'À emporter'),
    ]

    idcom = models.AutoField(primary_key=True)
    idplat = models.ForeignKey(Menu, on_delete=models.CASCADE)
    nomcli = models.CharField(max_length=100)
    typecom = models.CharField(max_length=10, choices=TYPE_CHOICES)
    idtable = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    datecom = models.DateTimeField(auto_now_add=True)
    quantite = models.IntegerField(default=1)

    def __str__(self):
        return f"Commande {self.idcom} - {self.nomcli}"


# ============================
# 🟦 RESERVATION
# ============================
class Reserver(models.Model):
    idreserv = models.AutoField(primary_key=True)
    idtable = models.ForeignKey(Table, on_delete=models.CASCADE)
    date_de_reserv = models.DateTimeField(auto_now_add=True)
    date_reserve = models.DateTimeField()
    nomcli = models.CharField(max_length=100)

    def __str__(self):
        return f"Réservation {self.idreserv} - {self.nomcli}"
