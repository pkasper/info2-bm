import abc

class ErrorCalculator(metaclass=abc.ABCMeta):
    """A class built to calculate errors on data series.
    This is an abstract class and thus, concrete implementations of the 
    error calculation methods have to be defined in the child classes.
    
    IMPORTANT: The predefined lengthcheck was changed. Both this and the
               old version will be accepted for submissions!
    
    Args:
      data (list): The series of true/test data. Can be of np.array(). 
                   This is the series of values you want to test against.

    Attributes:
      _data (str): The stored list of of true/test data. Only to be set
                   via the properties.
    """
    def __init__(self, data=list()):
        if self.__class__ is ErrorCalculator:
            raise NotImplementedError("Instantiated base class. Use a derivative!")
        self._data = data
        
    @property
    def data(self):
        """
        Property to access the true/test data. Can either be set in the class constructor
        or via this property. 
        
        TODO: The setter method should perform type safety checks! Best create a separate
        (non-abstract) function for this.
        """
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data

    @abc.abstractmethod
    def calc_error(self, y):
        """
        This method calculates the error of series y on the stored test data.
        
        TODO: Implement typechecks for y
        
        Args:
          y: The series to test with (against the values in self._data)

        Returns:
          The return value. The calculated error of series y on self_data
        """
        if self._data is None:
            raise ValueError("Data is not set")    
        if len(y) != len(self._data):
            raise ValueError("Series are not of identical length")