from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 30


class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def intersection_with(self, line2):
        try:
            A, B = self.normal_vector.coordinates
            C, D = line2.normal_vector.coordinates
            k1 = self.constant_term
            k2 = line2.constant_term

            x_numerator = D*k1 - B*k2
            y_numerator = -C*k1 + A*k2
            one_over_denom = Decimal('1.0')/(A*D - B*C)

            return Vector([x_numerator, y_numerator]).times_scalar(one_over_denom)
        
        except ZeroDivisionError:
            if self == line2:
                return self
        else:
            return None
        
    def is_parallel_to(self, line2):
        v1 = self.normal_vector
        v2 = line2.normal_vector
        return v1.is_parallel_to(v2)

    def __eq__(self, line2):
        ''' self and l2 are equal iff
            vector connect to self.base and line2.base [base1 - base2]
            vc is ortho to normal of self and normal of line2
        '''

        # if self.normal_vector().is_near_zero():
        #     if not line2.normal_vector.is_near_zero():
        #         return False
        #     else:
        #         diff = self.constant_term -line2.constant_term
        #         return MyDecimal(diff).is_near_zero()
        # elif line2.normal_vector().is_near_zero():
        #     return False

        if not self.is_parallel_to(line2):
            return False

        x0 = self.basepoint
        x1 = line2.basepoint
        basepoint_diff = x0.minus(x1)

        n = self.normal_vector
        return basepoint_diff.is_orthogonal_to(n)

    def intersects(self, line2):
        parallel = self.is_parallel_to(line2)
        if parallel :
            return False
        else:
            if self == line2:
                return False
            else:
                return True

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()


    def set_basepoint(self):
        try:
            n = self.normal_vector.coordinates
            c = self.constant_term
            basepoint_coords = ['0']*self.dimension

            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e


    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector.coordinates

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output


    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps