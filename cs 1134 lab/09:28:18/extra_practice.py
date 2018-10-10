class Polynomial:
    def __init__(self, list_of_coeffs=[0]):
        self.coefficients = list_of_coeffs
        # 0(n)

    def __repr__(self):
        return ' '.join([f'{self.coefficients[i]}x^{i} +' for i in range(len(self.coefficients) - 1, -1, -1) ])# if i > 0 else f'{self.coefficients[i]}'])
        # [:len(self.coefficients) * 7 - 6]
        # return str[0:]

    def eval(self, val):
        return sum(self.coefficients[i] * val**i for i in range(len(self.coefficients)))
        # 0(n)

    def __add__(self, other):
        if len(self.coefficients) > len(other.coefficients):
            length = len(other.coefficients)
            list = [self.coefficients[i] + other.coefficients[i] for i in range(length)]
            list.extend(self.coefficients[length:])
        else:
            length = len(self.coefficients)
            list = [self.coefficients[i] + other.coefficients[i] for i in range(length)]
            #0(n)
            list.extend(other.coefficients[length:])
            #0(m-n)
        return Polynomial(list) #0(n)

    def __mul__(self, other):
        list = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i in range(len(self.coefficients)):
            for e in range(len(other.coefficients)):
                list[i + e] = self.coefficients[i] * other.coefficients[e]
        return Polynomial(list)


import time
import random


class PolyTimer:
    def __init__(self):
        self.start = time.time()

    def elapsed(self):
        return time.time() - self.start

    def reset(self):
        self.start = time.time()


if __name__ == '__main__':
    poly1 = Polynomial([1, 2, 3, 4])
    #i = 5
    # str = f'1,2,3 {i}'
    # print(str)
    print(repr(poly1))
