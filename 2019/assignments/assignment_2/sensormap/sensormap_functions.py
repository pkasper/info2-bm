######################################################################
# Author: Malte Hupe
# MatNr: 1647577
# Description: Ass 2
# Comments: ---
######################################################################
import pandas, numpy

def read_cities(path, countries=[]):
    print(countries[0])
    colorcode = ['red', 'blue', 'green', 'purple', 'orange', 'darkred',\
             'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',\
             'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',\
             'gray', 'black', 'lightgray']
    citylist = []    
    data = pandas.read_csv(path)
    data.info()
    
    if len(countries) == 0:
            
        for index, row in data.iterrows():
            if row['city'] == "Stuttgart":
                print("Success")
                citylist.append(row['city'])
            
                #citylist.append(City(row['city'], Coordinates(row['lat'],row['lng']), row['population'], row['country'], colorcode))
    
        print(citylist)
        
       
       
        
        
        
    else:
       
        for index, row in data.iterrows():
            for i in countries:
                print(countries[i])
                if row['country'] == countries[i]:
                    print("Success")
                    citylist.append(row['city'])
                
                    #citylist.append(City(row['city'], Coordinates(row['lat'],row['lng']), row['population'], row['country'], colorcode))
        
        print(citylist)



def find_nearest_city(cities, coords):
    print("Hello")

def parse_sensors(data_path, cities):
    print("Hello")

def create_map(plot_list, filename, plot_sensor_values=False, smooth=False, zoom=10):
    print("Hello")
