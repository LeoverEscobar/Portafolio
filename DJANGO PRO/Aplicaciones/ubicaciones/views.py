from django.shortcuts import render
from .models import Lugares
import folium
from folium.plugins import FastMarkerCluster

# Create your views here.
def sitios(request):
    #Get my locations
    locations = Lugares.objects.all()
    #Define the initial map
    initialMap = folium.Map(location=[4.710989,-74.072090], zoom_start=15)
    #Creating the markets
    latitudes = [location.lat for location in locations]
    longitudes = [location.lng for location in locations]
    popups = [location.name for location in locations]
    FastMarkerCluster(data=list(zip(latitudes, longitudes, popups))).add_to(initialMap)
    
    #context = {'map':initialMap._repr_html_()}
    context = {'map':initialMap._repr_html_(), 'locations':locations}
    
    return render(request, 'mapa.html',context )