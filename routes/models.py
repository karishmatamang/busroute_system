from django.db import models
from bus.models import Bus

class Routes(models.Model):
    route_name=models.CharField(max_length=250)
    route_number=models.IntegerField()
    number_of_bus=models.IntegerField(null=True,blank=True)
    bus=models.ManyToManyField(Bus, through='BusRoutes')
    
    def __str__ (self):
        return self.route_name

class BusRoutes(models.Model):
    route=models.ForeignKey(Routes,on_delete=models.CASCADE)
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE)
    from_time=models.DateTimeField()
    to_time=models.DateTimeField()

    
