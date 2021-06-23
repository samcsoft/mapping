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
elev = list(data["ELEV"])

def color_producer(elev):
    result = 'lightgray'
    if elev < 1000:
        result = "orange"
    elif elev < 3000:
        result = "blue"
    elif elev < 7000:
        result = "darkblue"
    else:
        result = "purple"
    
    return result

for lat, lon, loc, stat, ele, in zip(latit, long, location, status, elev):
    v_location = "Location: " + loc + "; Status: " + stat
    fg.add_child(folium.Marker(location = [lat, lon], popup=v_location, icon=folium.Icon(color=color_producer(ele))))

map.add_child(fg)

map.save("map.html")