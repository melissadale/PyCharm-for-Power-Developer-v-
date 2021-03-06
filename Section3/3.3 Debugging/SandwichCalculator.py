import numpy
from random import randint


class Calculator:
    def __init__(self, my_cost):
        self.charge = 0
        self.my_cost = my_cost

    def markup(self):
        weights = numpy.random.random((3, 3))
        x = randint(0, 2)
        y = randint(0, 2)
        today_weight = weights[x][y] +1
        self.charge = self.my_cost * today_weight
        return self.charge

    def family_discount(self):
        self.charge = self.my_cost * 0.75
        return round(self.charge, 2)
