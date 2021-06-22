import  folium
from folium.map import Icon, Popup
import pandas as pd

data = pd.read_csv("Volcanoes.txt")

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name='The Map')

long = list(data["LON"])
latit = list(data["LAT"])
location = list(data["LOCATION"])
status = list(data["STATUS"])



for lat, lon, loc, stat in zip(latit, long, location, status):
    v_location = "Location: " + loc + "; Status: " + stat
    fg.add_child(folium.Marker(location = [lat, lon], popup=v_location, icon=folium.Icon(color='blue')))

map.add_child(fg)

map.save("map.html")