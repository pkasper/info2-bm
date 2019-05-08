######################################################################
# Author: Malte Hupe
# MatNr: 1647577
# Description: Ass 2
# Comments: ---
######################################################################
import pandas
import numpy as np
import folium
from folium.plugins import MarkerCluster

from .coordinates import Coordinates
from .sensor import Sensor
from .city import City

def read_cities(path, countries=[]):
    countries =  [c.lower() for c in countries]
    
    colorcode = ['red', 'blue', 'green', 'purple', 'orange', 'darkred',\
             'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',\
             'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',\
             'gray', 'black', 'lightgray']
    citylist = []    
    data = pandas.read_csv(path)
    
    if len(countries) == 0:
        
        for index, row in data.iterrows():
            citylist.append(City(row['city'], Coordinates(row['lat'],row['lng']), row['population'], row['country'], np.array2string(np.random.choice(colorcode))))

                  
    else:
       
        for index, row in data.iterrows():
            if row['country'].lower() in countries:           
                citylist.append(City(row['city'], Coordinates(row['lat'],row['lng']), row['population'], row['country'],  np.array2string(np.random.choice(colorcode))))
        
    return citylist
            


def find_nearest_city(cities, coords):

    distance = np.inf
    nearest_city = None

    for city in cities:

        if Coordinates.distance(coords, city.coords) < distance and Coordinates.distance(coords, city.coords) < 10:
            distance = Coordinates.distance(coords, city.coords)
            nearest_city = city

    return nearest_city
        

def parse_sensors(data_path, cities):
    
    sensorlist = []
    sensor_data = pandas.read_csv(data_path)
    
    for index, row in sensor_data.iterrows():
        city_obj = find_nearest_city(cities, Coordinates(row['lat'],row['lon']))
        if city_obj != None:
            sensorlist.append(Sensor(row['sensor_id'], city_obj, Coordinates(row['lat'],row['lon']), data))
        
    return sensorlist
    

def create_map(plot_list, filename, plot_sensor_values=False, smooth=False, zoom=10):
    m = folium.Map(
        location=[48.023439, 11.590285],
        height=1000,
        width=1000, 
        zoom_start= zoom
    )
    mc = MarkerCluster(overlay=True, control=True)
    
    for obj in plot_list:
        
        if isinstance(obj, City) is False and isinstance(obj, Sensor) is False: 
            raise TypeError("Input a City-object or Sensor-object!")
     
    
        mc.add_child(folium.Marker(
            [obj.coords.lat, obj.coords.lon], 
            popup='<b>Timberline Lodge</b>', 
            #tooltip=tooltip
        )).add_to(m)

        

    # popup = folium.Popup(
    #     folium.IFrame(
    #         folium.Html(
    #             Sensor.create_bokeh_plot()
    #         ),
    #         height=325,
    #         width=425
    #     ), 
    #     max_width=425
    # )

    
        
    m.save(filename)
    