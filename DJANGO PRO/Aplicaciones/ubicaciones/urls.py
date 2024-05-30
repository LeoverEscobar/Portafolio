from django.urls import path
from . import views

urlpatterns = [ 
    path("ubicaciones/", views.sitios, name="ubicaciones"),
]


#https://www.latlong.net/convert-address-to-lat-long.html
