######################################################################
# Author: Malte Hupe
# MatNr: 1647577
# Description: Ass 2
# Comments: ---
######################################################################
import os
from sensormap import City, Coordinates,Sensor, read_cities, parse_sensors, create_map

obj1 = Coordinates("48.021329", "11.594557")
obj2 = Coordinates(48.023439, 11.590285)
obj3 = "1"

print(Coordinates.distance(obj1, obj2))

path = os.path.abspath(".")+"/worldcities.csv"
read_cities(path, ["Deutschland"])#"Deutschland"

