from django_tables2.utils import A, Accessor
import django_tables2 as tables
from .models import Routes, BusRoutes

class RoutesTable(tables.Table):
    number_of_bus = tables.columns.LinkColumn('busroute', args=[A('pk')] )
    class Meta:
        model = Routes
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-striped table-hover"}    
        fields = ("route_name","route_number" ,"number_of_bus")
    

class BusRoutesTable(tables.Table):
    bus_number=tables.Column(accessor=Accessor('bus.bus_number'))
    class Meta:
        model = BusRoutes
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-striped table-hover"}    
        fields = ("bus","bus_number","from_time","to_time" )
