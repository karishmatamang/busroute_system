from django.db import models

class Bus(models.Model):
    bus_name=models.CharField(max_length=250)
    bus_number=models.IntegerField(unique=True)
    number_of_routes=models.IntegerField(null=True,blank=True)

    def __str__ (self):
        return self.bus_name


