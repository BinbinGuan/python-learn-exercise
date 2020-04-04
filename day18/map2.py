import json

import folium
import requests

url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
antarctic_ice_edge = f'{url}/antarctic_ice_edge.json'
antarctic_ice_shelf_topo = f'{url}/antarctic_ice_shelf_topo.json'


m = folium.Map(
    location=[80.6016, 120],
    tiles='Mapbox Bright',
    zoom_start=2  # Limited levels of zoom for free Mapbox tiles.
)

folium.GeoJson(
    antarctic_ice_edge,
    name='geojson'
).add_to(m)

folium.TopoJson(
    json.loads(requests.get(antarctic_ice_shelf_topo).text),
    'objects.antarctic_ice_shelf',
    name='topojson'
).add_to(m)

folium.LayerControl().add_to(m)


m.save("test2.html")