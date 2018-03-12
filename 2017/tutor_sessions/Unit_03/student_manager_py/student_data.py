
# coding: utf-8

# In[ ]:

class StudentData:
    """Provides convinient access methods
    
    """
    def __init__(self,students):
        self._students = students
    @property
    def data(self):
        return self._students
    
    def get_student_by_matriclenumber(self,matriclenumber):
        return self._students[matriclenumber]

