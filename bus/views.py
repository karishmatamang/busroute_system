from django.shortcuts import render
from bus.models import Bus
from bus.tables import BusTable,RouteBusTable
from routes.models import BusRoutes

def bus(request):
    bus=Bus.objects.all()
    route=BusRoutes.objects.all()
    for buss in bus:
        total=0
        for routes in route:
            if buss.id==routes.bus.id:
                total+=1
        Bus.objects.filter(id=buss.id).update(number_of_routes=total)
    table=BusTable(Bus.objects.all())
    return render(request,'bus/bus.html', {"table": table})

def routebus(request,pk):
    bus=Bus.objects.get(pk=pk)
    table=RouteBusTable(BusRoutes.objects.filter(bus=bus.id).all())
    return render(request,'bus/routebus.html', {"table": table})
