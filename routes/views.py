from django.shortcuts import render,redirect
from routes.tables import RoutesTable,BusRoutesTable
from routes.models import Routes,BusRoutes
from bus.models import Bus

def home(request):
    return render(request,'home.html')

def route(request):
    buss=Routes.objects.all()
    for i in buss:
        itemscount= i.bus.all().count()
        Routes.objects.filter(id=i.id).update(number_of_bus=itemscount)             
    table=RoutesTable(Routes.objects.all())
    return render(request,'routes/route.html', {"table": table})

def busroute(request,pk):
    route=Routes.objects.get(pk=pk)
    table=BusRoutesTable(BusRoutes.objects.filter(route=route.id).all())
    return render(request,'routes/busroute.html', {"table": table})


