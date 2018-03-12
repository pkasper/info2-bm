
# coding: utf-8

# In[ ]:

from .student_parser import StudentParser
from .student_data import StudentData

class StaticParser(StudentParser):
    """A static data provider class
    
    Mainly for testing purposes
    """
    def read_data(self,options=""):
        student_dict = {"1234124",("1234124","Julia Musterfrau","KFU GRAZ")}
        self._student_data = StudentData(student_dict)
        return True

