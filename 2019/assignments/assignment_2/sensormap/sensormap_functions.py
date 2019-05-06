######################################################################
# Author: Malte Hupe
# MatNr: 1647577
# Description: Ass 2
# Comments: ---
######################################################################
import pandas
import numpy as np
from .coordinates import Coordinates
from .city import City

def read_cities(path, countries=[]):
    countries =  [c.lower() for c in countries]
    print(countries[0])
    colorcode = ['red', 'blue', 'green', 'purple', 'orange', 'darkred',\
             'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',\
             'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',\
             'gray', 'black', 'lightgray']
    citylist = []    
    data = pandas.read_csv(path)

    
    if len(countries) == 0:
        
        for index, row in data.iterrows():
            citylist.append(City(row['city'], Coordinates(row['lat'],row['lng']), row['population'], row['country'], np.random.choice(colorcode)))

                  
    else:
       
        for index, row in data.iterrows():
            if row['country'].lower() in countries:           
                citylist.append(City(row['city'], Coordinates(row['lat'],row['lng']), row['population'], row['country'], np.random.choice(colorcode)))
        
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
    data = pandas.read_csv(data_path)
    print(data)
    
    #find_nearest_city(cities, coords)
    

def create_map(plot_list, filename, plot_sensor_values=False, smooth=False, zoom=10):
    pass
