from django.urls import path
from bus.views import bus,routebus

urlpatterns = [
    path('',bus),
    path('<int:pk>/',routebus, name='routebus'),
]
