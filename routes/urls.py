from django.urls import path
from routes.views import home, route
from routes.views import busroute


urlpatterns = [
    path('',home ),
    path('routes/',route),
    path('routes/<int:pk>/',busroute, name='busroute')
]
