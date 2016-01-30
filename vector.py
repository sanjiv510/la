#! /usr/bin/python -tt

from math import degrees, pi, sqrt, acos, sin, cos
#from cmath import sqrt, acos, sin, cos
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            print "coordinates: ", coordinates
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        a_tuple = tuple(["{:.3f}".format(n) for n in self.coordinates])
        return 'Vector: {}'.format(a_tuple)

    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    def cross(self, w):
        
        if self.dimension<3:
            x = Vector(self.coordinates+('0',)).coordinates
            y = Vector(w.coordinates+('0',)).coordinates
        else:
            x = self.coordinates
            y = w.coordinates
        
        
        new_coordinates = [x[1]*y[2] - x[2]*y[1], -(x[0]*y[2] - x[2]*y[0]), x[0]*y[1] - x[1]*y[0]]
        return Vector(new_coordinates)

    def area_parallogram(self, v):
        x_product = self.cross(v)
        return x_product.magnitude()

    def area_tringle(self, v):
        return self.area_parallogram(v)/Decimal('2.0')

    def component_orthogonal_to(self, basis):
        projection = self.component_parallel_to(basis)
        return self.minus(projection)

    def component_parallel_to(self, basis):
        basis_unit  = basis.normalized()
        mag_parallel = self.dot(basis_unit)
        return basis_unit.times_scalar(mag_parallel)

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v))< tolerance

    def is_parallel_to(self, v):
        return ( self.is_zero() or
                v.is_zero() or
                self.angle_with_rad(v) == 0 or
                self.angle_with_rad(v) == pi)
    # def is_parallel_to(self, v):
    #      self_normal = self.normalized()
    #      v_normal = v.normalized()
    #      return self_normal == v_normal or self_normal == v.times_scalar(-1)

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def dot(self,v):
        new_coordinates = [x*y for x, y in zip(self.coordinates, v.coordinates) ]
        return sum(new_coordinates)
    
    def angle_with_rad(self,v):
            dot = self.dot(v)
            magnitude_product = self.magnitude()*v.magnitude()
            try:
                return acos(round(dot/magnitude_product,10))
            except Exception as e:
                if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                    raise Exception('Cannot compute an angle with the zero vector')
                else:
                    raise e
    
    def angle_with_deg(self, v):
        rad = self.angle_with_rad(v)
        return degrees(rad)

    def plus(self, v):
        new_coordinates = [x+y for x, y in zip(self.coordinates, v.coordinates) ]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x, y in zip(self.coordinates, v.coordinates) ]
        return Vector(new_coordinates)


    def times_scalar(self, c):
        new_coordinates = [x*Decimal(c) for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        coordinates_squared = [Decimal(x**2) for x in self.coordinates]
        x = sqrt(sum(coordinates_squared))
        return Decimal(x)

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal(1.0)/magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
