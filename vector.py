#! /usr/bin/python -tt

import math as math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def times(self, c):
        new_coordinates = [x*c for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        side_sqrs = [x*x for x in self.coordinates]
        return math.sqrt(sum(side_sqrs))

    def direction(self):
        mag = self.magnitude()
        return self.times(1/mag)
