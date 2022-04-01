from turtle import *
from math import *

# Librarie pour des vecteurs 2D

class Vec:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, k):
        return Vec(self.x * k, self.y * k)
    
    def __rmul__(self, k):
        return self.__mul__(k)
    
    def __truediv__(self, k):
        return Vec(self.x / k, self.y / k)

    def __str__(self):
        return f'Vec({self.x}, {self.y})'

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __neg__(self):
        return Vec(-self.x, -self.y)
    
    def normalize(self):
        d = abs(self)
        self.x /= d
        self.y /= d
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
    
    def draw(self):
        p = pos()
        q = Vec(p)
        towards(self.p)
    
if __name__ == '__main__':
    a = Vec(30, 40)
    b = Vec(10, 20)

    alpha = towards(a.x, a.y)
    seth(alpha)
    goto(a.x, a.y)
    stamp()
    
    print(alpha)
    
    
#     print('a =', a)
#     print('b =', b)
#     print('a + b =', a + b)
#     print('a - b =', a - b)
#     print('2 * a =' , 2 * a)
#     print('a * 2 =' , a * 2)
#     print('a / 2 =' , a / 2)
#     print('abs(a) =' , abs(a))
#     print('a.dot(b) =' , a.dot(b))
#     print('-a =', -a)
#     
#     a.normalize()
#     print('a.normalize()', a)
#     print(abs(a))
#     a.draw()
    
    done()