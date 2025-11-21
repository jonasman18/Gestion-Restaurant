from django.shortcuts import render

@api_view(['GET'])
def clients_par_date(request):
    date = request.GET.get('date')
    start = request.GET.get('start')
    end = request.GET.get('end')

    qs = Commander.objects.all()

    if date:
        qs = qs.filter(datecom__date=date)

    if start and end:
        qs = qs.filter(datecom__date__range=[start, end])

    return Response(CommandeSerializer(qs, many=True).data)

