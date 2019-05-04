######################################################################
# Author: Malte Hupe
# MatNr: 1647577
# Description: Ass 2
# Comments: ---
######################################################################

import math
            
class Coordinates:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, value):
        try:
            value = float(value)
        
        except:
            raise TypeError("Input a float!") 
            

        if (value <= 90 and value > -90):
            self._lat = value

        else:
            raise ValueError("Input a Number between -90/90!") 


    @property
    def lon(self):
        return self._lon

    @lon.setter
    def lon(self, value):

        try:
            value = float(value) 
        
        except:
            raise TypeError("Input a float!")  

        if (value <= 180 and value > -180):
            self._lon = value

        else:
            raise ValueError("Input a Number between -180/180!") 
                   
        
        



    @classmethod
    def distance(cls, coord_1, coord_2):
        #rueckgabe als float
        lat1 = coord_1.lat
        lat1 = coord_1.lon
        lon2 = coord_2.lat
        lat2 = coord_2.lon

        distance = float(6371 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)))
        return distance

    

#class city


Bewertungsobjekt = Coordinates("48.021329", "11.594557")
print(Bewertungsobjekt.lat)
print(Bewertungsobjekt.lon)
Coordinates.distance(Bewertungsobjekt, Bewertungsobjekt)


