import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def diffrent_colors(elevation):
    if elevation < 1000:
        return "green"
    elif 1000<= elevation < 3000:
        return "orange"
    else:
        return "blue"
map = folium.Map(location=[11.24, 80.40],zoom_start=5)

fgv = folium.FeatureGroup("Volcanoes")
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln],radius=7,popup=str(el)+" m",fill_color=diffrent_colors(el),color="black",fill_opacity=0.7))
    #fg.add_child(folium.RegularPolygonMarker(location=[lt, ln],number_of_sides=4,radius=7,popup=str(el)+" m",fill_color=diffrent_colors(el),color="black",fill_opacity=0.7))
fgp = folium.FeatureGroup("Population")
fgp.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else "red" if 10000000<=x['properties']['POP2005']<20000000 else "blue"}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
