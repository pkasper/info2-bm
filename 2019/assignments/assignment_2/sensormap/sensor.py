######################################################################
# Author: Malte Hupe
# MatNr: 1647577
# Description: Ass 2
# Comments: ---
######################################################################
from geopy.geocoders import ArcGIS
from bokeh.plotting import figure
from bokeh.models import Band, HoverTool, ColumnDataSource

from .coordinates import Coordinates

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
        if self._address is None:
            self._address = geolocator.reverse((self.coords.lat, self.coords.lon)).address
        return self._address  

    
    def create_bokeh_plot(self, smooth=False):
        data = self.data.copy(deep=True)
        if smooth == True:
            data[['P1', 'P2']] = data.rolling(smooth, on="timestamp").mean()[['P1', 'P2']]
    

        source = ColumnDataSource(data)
        bokehfig = figure(title="Sensor:"+self.id, x_axis_label='Time in d', y_axis_label='y', x_label_type='datetime', plot_width='400px', plot_height='300px')
        p1 = bokehfig.line(x="timestamp", y="P1", line_width=1, source=source)
        p2 = bokehfig.line(x="timestamp", y="P2", line_width=1, source=source)

        bokehfig_hovertool = HoverTool(
            tooltips=[
                ( 'date',   '@timestamp{%F}' ),
                ( 'p1',  '@P1' ),
                ( 'p2',  '@P2' ),
            ],

            mode='vline',
            point_policy = 'follow_mouse',
            renderers = [p1]
        )

        band1 = Band(base='timestamp', lower=0, upper='P1', line_width=3, fill_color='orange', line_color='orange', source=source)
        band2 = Band(base='timestamp', lower=0, upper='P2', line_width=3, fill_color='blue', line_color='blue', source=source)

        bokehfig.add_layout(band1)
        bokehfig.add_layout(band2)
        bokehfig.add_tools(bokehfig_hovertool)

        return bokehfig