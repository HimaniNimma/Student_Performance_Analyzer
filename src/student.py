import numpy as np

class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def average(self):
        return np.mean(list(self.marks.values()))