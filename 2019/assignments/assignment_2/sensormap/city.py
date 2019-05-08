######################################################################
# Author: Malte Hupe
# MatNr: 1647577
# Description: Ass 2
# Comments: ---
######################################################################
#from .sensor import Sensor
from .coordinates import Coordinates

class City:
    def __init__(self, name, coords, population, country, colorcode):
        if type(name) == str:
            self._name = name

        else: 
            raise TypeError("Input a string!")
        
        if isinstance(coords, Coordinates):
            self._coords = coords
        else:
            raise TypeError("Input an Coordinates-object!")

        try:
            self._population = float(population) 
        
        except:
            raise TypeError("Input a float!")  

        if type(country) == str:
            self._country = country

        else: 
            raise TypeError("Input a string!")
        
        if type(colorcode) == str:
            self._colorcode = colorcode

        else: 
            raise TypeError("Input a string!")



    @property
    def name(self):
        return self._name
    
    @property
    def population(self):
        return self._population
    
    @property
    def coords(self):
        return self._coords
    
    @property
    def country(self):
        return self._country
    
    @property
    def sensors(self):
        return self._sensors
    
    @property
    def colorcode(self):
        return self._colorcode
    
    @colorcode.setter
    def colorcode(self, value):
        self._colorcode = value

        
        
    def add_sensor(self, sensor):

        if isinstance(sensor, Sensor):
            self._sensors.append(sensor)
        else:
            raise TypeError("Input a Sensor-Object!")#Inputerror?

        
        
