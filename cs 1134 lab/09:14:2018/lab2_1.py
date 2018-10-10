'''
We will represent a
polynomial as a list of its coefficients, as a data member. The first element in the list
represents the constant, while each of the next elements represents the coefficient of the
next power in your polynomial.
Note: the length of the coefficient list used to represent p(x) is 1+deg(p), where deg(p) is
the degree of the polynomial p (the largest power in p with a non-zero coefficient)
'''


class Polynomial:
    def __init__(self, list_of_coeffs=[0]):
        self.coefficients = list_of_coeffs

    def __repr__(self):
        return ' '.join([f'{self.coefficients[i]}x^{i} +' for i in range(len(self.coefficients) - 1, -1, -1) if i > 0 else f'{self.coefficients[i]}'])
        # [:len(self.coefficients) * 7 - 6]
        # return str[0:]

    def eval(self, val):
        return sum(self.coefficients[i] * val**i for i in range(len(self.coefficients)))

    def __add__(self, other):
        if len(self.coefficients) > len(other.coefficients):
            length = len(other.coefficients)
            list = [self.coefficients[i] + other.coefficients[i] for i in range(length)]
            list.extend(self.coefficients[length:])
        else:
            length = len(self.coefficients)
            list = [self.coefficients[i] + other.coefficients[i] for i in range(length)]
            list.extend(other.coefficients[length:])
        return Polynomial(list)

    def __mul__(self, other):
        list = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i in range(len(self.coefficients)):
            for e in range(len(other.coefficients)):
                list[i + e] = self.coefficients[i] * other.coefficients[e]
        return Polynomial(list)

    def derive(self):
        list = [0] * (len(self.coefficients) - 1)
        # cannot assign before I initialize list?
        for i in range(1, len(self.coefficients)):
            list[i - 1] = self.coefficients[i] * i
        print(list)
        return Polynomial(list)


if __name__ == '__main__':
    poly1 = Polynomial([1, 2, 3, 4])
    poly2 = Polynomial([1, 2])
    print(repr(poly1))
    name = 'Ly'
    str = f'{name} is my name'
    # print(str)
    print(poly1.eval(2))
    print(repr(poly1 + poly2))
    print(repr(poly1 * poly2))
    print(repr(poly1.derive()))
# if sth == 0: return ...
