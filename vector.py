#! /usr/bin/python -tt

from math import sqrt, acos, degrees, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot_product(v))< tolerance

    def is_parallel_to(self, v):
        return ( self.is_zero() or
                v.is_zero() or
                self.angle_in_rad(v) == 0 or
                self.angle_in_rad(v) == pi)
    # def is_parallel_to(self, v):
    #      self_normal = self.normalized()
    #      v_normal = v.normalized()
    #      return self_normal == v_normal or self_normal == v.times_scalar(-1)

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def dot_product(self,v):
        new_coordinates = [x*y for x, y in zip(self.coordinates, v.coordinates) ]
        return sum(new_coordinates)
    
    def angle_in_rad(self,v):
            dot_product = self.dot_product(v)
            magnitude_product = self.magnitude()*v.magnitude()
            try:
                return acos(dot_product/magnitude_product)
            except ZeroDivisionError:
                raise 'One of the magnitude is zero, to get angle both vector magnitude should be greter than zero'
    
    def angle_in_deg(self, v):
        rad = self.angle_in_rad(v)
        return degrees(rad)

    def plus(self, v):
        new_coordinates = [x+y for x, y in zip(self.coordinates, v.coordinates) ]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x, y in zip(self.coordinates, v.coordinates) ]
        return Vector(new_coordinates)


    def times_scalar(self, c):
        new_coordinates = [x*c for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return Decimal(sqrt(sum(coordinates_squared)))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal('1.0')/magnitude)
        except ZeroDivisionError:
            raise Exception('Cannot normalize zero vector')
