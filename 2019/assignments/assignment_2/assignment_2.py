######################################################################
# Author: Malte Hupe
# MatNr: 1647577
# Description: Ass 2
# Comments: ---
######################################################################
import os
from sensormap import City, Coordinates, Sensor, read_cities, parse_sensors, create_map, find_nearest_city

obj1 = Coordinates("48.021329", "11.594557")
obj2 = Coordinates(48.023439, 11.590285)
obj3 = Coordinates(48.124079, 11.567699)


#print(Coordinates.distance(obj1, obj2))

#path = os.path.abspath(".")
path = "/Users/mcdon/Downloads/ass_2_files"

cities = read_cities(path+"/worldcities.csv", ["Germany"])
sensors = parse_sensors(path+"/sensors_ass_2_small.csv", read_cities(path+"/worldcities.csv", ["Germany"]))

x = find_nearest_city(cities, Coordinates(48.124079, 11.567699))
print(x)
cities.append(x)
create_map(parse_sensors, "index.html")