import folium

# 地图
m = folium.Map(location=[31.22, 121.48])
m.save('index.html')

#显示黑白的街道
# b = folium.Map(
#     location=[31.22, 121.48],
#     tiles='Stamen Toner',
#     zoom_start=10
# )
# b.save('index_test1.html')


# 点击显示精度
# shenqiu = folium.Map(
#     location=[33.41, 115.06],
#     tiles='Stamen Terrain',
#     zoom_start=13
# )
# shenqiu.add_child(folium.LatLngPopup())
# shenqiu.save('shenqiu.html')
#


# 标记
mar = folium.Map(
    location=[33.41, 115.06],
    tiles='Stamen Terrain',
    zoom_start=13
)
folium.Marker(
    [33.41, 115.06],
    popup='Camp Muir'
).add_to(mar)

mar.add_child(folium.ClickForMarker(popup='Waypoint'))
mar.save('mar.html')
