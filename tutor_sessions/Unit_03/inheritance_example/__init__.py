"""
This is a basic example of creating a package

In this package, a basic human - student inheritance is showed
"""

#Reference for from inheritance_example import *
__all__ = ['human', 'student']

#Include the submodules
from .human import Human
from .student import Student

