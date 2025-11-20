from reportlab.pdfgen import canvas
from django.http import HttpResponse
from restaurant.models import Commande


def facture_pdf(request, idcom):
    try:
        commande = Commande.objects.get(pk=idcom)
    except Commande.DoesNotExist:
        return HttpResponse("Commande introuvable.", status=404)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="facture_{idcom}.pdf"'

    p = canvas.Canvas(response)
    p.setTitle("Facture Restaurant")

    p.drawString(100, 800, "NOM DU RESTAURANT")
    p.drawString(100, 780, f"Code Commande : {commande.idcom}")
    p.drawString(100, 760, f"Client : {commande.nomcli}")

    if commande.idtable:
        p.drawString(100, 740, f"Table : {commande.idtable.designation}")
    else:
        p.drawString(100, 740, "Commande à emporter")

    p.drawString(100, 700, "Menu        PU       Qte      Total")
    p.drawString(
        100, 680,
        f"{commande.idplat.nomplat}     {commande.idplat.pu}     {commande.quantite}     {commande.total()}"
    )

    p.drawString(100, 640, f"TOTAL À PAYER : {commande.total()} Ariary")

    p.showPage()
    p.save()
    return response
