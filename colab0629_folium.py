# -*- coding: utf-8 -*-
"""colab0629_folium.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eAR1wN3yLVGKs5QPpApBmSqOrPRzueBk

Folium
"""

import folium

loc = folium.Map()
loc

loc = folium.Map(location=[37.546817, 126.911411],
                 zoom_start=15)
loc

loc.save('map.html')

import os
path = os.getcwd()
os.listdir(path)

# 31.203305966003168, 121.43267590923834

loc = folium.Map(location=[31.203305966003168, 121.43267590923834], zoom_start=15)

folium.Marker([31.203305966003168, 121.43267590923834]).add_to(loc) # 학교
folium.Marker([31.193694194343692, 121.43687690583062]).add_to(loc) # 집
loc

m = folium.Map(
    location=[46.59379025138313, 2.8674244657960717],
    zoom_start=3
)

folium.Marker(
    location=[65.03855307257587, -18.808363969692863],
    popup = 'Island',                         # 선택 시 popup
    icon = folium.Icon(color='blue', icon="info-sign") # 아이콘  # glyphicon-check, star
).add_to(m)

folium.Marker(
    location=[55.15292742379517, -7.9735022614721185],
    popup = 'Ireland',                       
    icon = folium.Icon(color='green', icon="info-sign")
).add_to(m)

folium.Marker(
    location=[39.069256415134696, 35.36540147551945],
    popup = 'Turkey',                        
    icon = folium.Icon(color='red', icon="info-sign")
).add_to(m)

folium.Marker(
    location=[42.23376707888608, 43.32227790734392],
    popup = 'Georgia',                         
    icon = folium.Icon(color='lightgray', icon="info-sign")
).add_to(m)

folium.Marker(
    location=[24.136850625842516, -102.42797168153588],
    tooltip = '멕시코',                         
    icon = folium.Icon(color='purple', icon="info-sign")
).add_to(m)

m

## (실습) CircleMarker추가. 동교동, 신촌동 중심으로 추가하기. 중심은 동교동으로 하기

m = folium.Map(
    location=[37.55739849387253, 126.92260544181],
    zoom_start=15
)

folium.CircleMarker(
    location=[37.55739849387253, 126.92260544181],
    radius = 100,
    color = '#ffffgg',
    fill_color='#fffggg',
    tooltip = '동교동',                         # 선택 시 popup
).add_to(m)

folium.CircleMarker(
    location=[37.564132396654585, 126.93873269150986],
    radius = 80,
    color = '#ffffgg',
    fill_color='#fffggg',
    tooltip = '신촌동',                        
).add_to(m)

m

from folium import plugins

import numpy as np
import os

N = 100

data = np.array(
    [
     np.random.uniform(low=35, high=60, size=N),
     np.random.uniform(low=-12, high=30, size=N),
    ]
).T

print(data[0:10])

popups = [str(i) for i in range(N)]

m = folium.Map([45, 3], zoom_start=4) 
plugins.MarkerCluster(data, popups=popups).add_to(m) 

m

## 5-2 (실습) 우리나라 지역에 50군데 데이터를 만들고, markerCluster를 이용하여 지도 시각화를 해보자.

# 경도 : 125.06666667 ~ 131.87222222
# 위도 : 33.10000000 ~ 38.45000000

N = 50

data = np.array(
    [
     np.random.uniform(low=34.418, high=38.667, size=N),
     np.random.uniform(low=126.63, high=129.55, size=N),
    ]
).T

print(data)

popups = [str(i) for i in range(N)]

m = folium.Map([36.5981, 128.7247], zoom_start=10) 
plugins.MarkerCluster(data, popups=popups).add_to(m) 

m

m.save(os.path.join('.', 'Plugins_1.html'))

import folium

m = folium.Map(
    location=[37.5838699,127.0565831],
    zoom_start=10
)

import json
with open('seoul_muncipalities_geo.json',mode='rt',encoding='utf-8') as f:
    geo = json.loads(f.read())
    f.close()

folium.GeoJson(
    geo,
    name='seoul_municipalities'
).add_to(m)

m.save('map.html')
m

stamen = folium.Map(location=[45.5236, -122.6750],
                    tiles='Stamen Toner', 
                    zoom_start=13)
stamen

stamen = folium.Map(location=[45.5236, -122.6750],
                    tiles='Stamen Terrain', 
                    zoom_start=13)
stamen