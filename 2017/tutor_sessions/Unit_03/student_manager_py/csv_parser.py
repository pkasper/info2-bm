
# coding: utf-8

# In[1]:

from .student_parser import StudentParser
from .student_data import StudentData
import csv

class CSVParser(StudentParser):
    def read_data(self,options):
        student_dict = {}
        f = open(options, 'rt')
        try:
            reader = csv.reader(f)
            for row in reader:
                student_dict[row[0]] = (row[0],row[1],row[2])
        except:
            return False
        finally:
            f.close()
        self._student_data = StudentData(student_dict)
        return True

