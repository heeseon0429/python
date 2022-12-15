import cx_Oracle
import folium
import os
conn = cx_Oracle.connect('scott', 'tiger', 'localhost/xe')
cursor = conn.cursor()
sql = 'SELECT * FROM jadam'
cursor.execute(sql)
list = cursor.fetchall()
os.makedirs('map', exist_ok=True)
map_osm = folium.Map(location=[37.572807, 126.975918], zoom_start=7)  # tiles='Stamen Terrain'/ 'Stamen

for x in list:
    print(x)
    folium.Marker(location=[x[3], x[4]], popup=x[0], icon=folium.Icon(color='red', icon='info-sign')).add_to(map_osm)

map_osm.save('./map/jadamMap.html')