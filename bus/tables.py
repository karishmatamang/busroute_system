from django_tables2 import tables
from django_tables2.utils import A,Accessor
from bus.models import Bus
from routes.models import Routes,BusRoutes

class BusTable(tables.Table):
    number_of_routes = tables.columns.LinkColumn('routebus', args=[A('pk')] )
    class Meta:
        model = Bus
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-striped table-hover"}    
        fields = ("bus_name","bus_number","number_of_routes" )

class RouteBusTable(tables.Table):
    route_number=tables.columns.Column(accessor=Accessor('route.route_number'))
    class Meta:
        model = BusRoutes
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-striped table-hover"}        
        fields = ("route","route_number","from_time","to_time" )