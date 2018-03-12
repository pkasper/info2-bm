
# coding: utf-8

# In[1]:

class StudentParser:
    """Abstract base class
    
    """
    def __init__(self):
        """Initializes the StudentParser Class
        
        Sets the data property to None
        """
        self._student_data = None
    def read_data(self,options=""):
        raise NotImplementedError
    @property
    def students(self):
        """Returns the student data dictionary
        """
        return self._student_data

