
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["NAME"])
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
"""
map = folium.Map(location=[38.59,-99.09],zoom_start=6,tiles = "Stamen Terrain")
fg=folium.FeatureGroup(name="My Map")
for lt,ln,name in zip(lat,lon,name):
    iframe = folium.IFrame(html=html % (name, name), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=5,popup=folium.Popup(iframe),color='red',icon=folium.Icon(color='red',fill_opacity=0.7)))
fg.add_child(folium.GeoJson(data=open("world.json","r",encoding='utf-8-sig').read(),
style_function=lambda x: {'fillcolor':'yellow'}))
map.add_child(fg)
map.save("Map-tes.html")
