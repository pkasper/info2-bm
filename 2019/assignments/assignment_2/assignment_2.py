######################################################################
# Author: Malte Hupe
# MatNr: 1647577
# Description: Ass 2
# Comments: ---
######################################################################

class Coordinates:
    def __init__(self, new_lat, new_lon):
        print("init")
        self.lat = new_lat
        self.lon = new_lon



    @property
    def lat(self):
        print("getter")
        return self._lat

    @lat.setter
    def lat(self, value):
        print("hi1")
        self._lat = value



    @property
    def lon(self):
        return self._lon

    @lon.setter
    def lon(self, value):
        print("hi2")
        self._lon = value



    @classmethod
    def distance(cls, coord_1, coord_2):
        #rueckgabe als float
        distance = 6371 * arccos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon2 - lon1))


    def is_float(value):
        print("Test")
        try:
            value = float(value)
            return value
        except ValueError:
            print ("Must be convertable to float!")


Bewertungsobjekt = Coordinates("1.111", "15.455678")
print(Bewertungsobjekt.lat)
Bewertungsobjekt.lat = 455678

print(Bewertungsobjekt.lat)
