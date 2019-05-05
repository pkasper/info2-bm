######################################################################
# Author: Malte Hupe
# MatNr: 1647577
# Description: Ass 2
# Comments: ---
######################################################################
from geopy.geocoders import ArcGIS
import bokeh, matplotlib

class Sensor:
    def __init__(self, sensor_id, city, coords, data):
        
        self._data = data
        self._address = None

        if type(sensor_id) == int:
            self._id = sensor_id

        else: 
            raise TypeError("Input a integer!")
        
        if isinstance(city, City):
            self._city = city
        else:
            raise TypeError("Input an City-Object!")
        
        if isinstance(coords, Coordinates):
            self._coords = coords
        else:
            raise TypeError("Input an Coordinates-Object!")

    
    
    @property
    def id(self):
        return self._id
    
    @property
    def city(self):
        return self._city
    
    @property
    def coords(self):
        return self._coords
    
    @property
    def distance_to_centre(self):
        return self._distance_to_centre   
    
    @property
    def data(self):
        return self._data   

    @property
    def address(self):
        first_call = True
        if first_call == True:
            self._address = geolocator.reverse((coords.lat, coords.lon)).address
            first_call = False
            
        else:
            return self._address  

    
    def create_bokeh_plot(self, smooth=False):
        if smooth == True:
            print("yes")
            #data[['P1', 'P2']] = data.rolling("30d", on="timestamp").mean()[['P1', 'P2']]
            
            #fill_between() von Matplotlib
            #Bokeh HoverTool um einen Mouseover Effekt bei den Popups   
            #HoverTools den Parameter mode auf ”vline” und den Parameter point_policy auf ”follow_mouse”.
            #binden Sie es nur an die Linie von P1 (die Sie zusätzlich zum Band geplottet haben). 
            # Dies können Sie mit dem Parameter renderers() beim HoverTool
            #Höhe des Bokeh Plots auf 300px, die Breite auf 400px
        else:
            print("no")