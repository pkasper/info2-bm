
# coding: utf-8

# In[1]:

from .csv_parser import CSVParser
from .static_parser import StaticParser

class StudentManager:
    """Main package class
    """
    def __init__(self, parser):
        """Constructor, initializes the StudentManager Class
        
        Valid arguments are: "csv" and "static"
        """
        if parser == "csv":
            self._parser = CSVParser()
        elif parser == "static":
            self._parser = StaticParser()
        else:
            raise NotImplementedError
    @property
    def parser(self):
        """Returns the used student_parser
        """
        return self._parser
    @property 
    def students(self):
        """Convinient function to access the parsed data object
        """
        return self._parser.students
    def read_data(self,options=""):
        """Makes the parsers read_data function available
        """
        return self._parser.read_data(options)

