from typing import Any
from math import sqrt


class Vec3(object):

    def __init__(self, e0=0, e1=0, e2=0) -> None:
        self.x = e0
        self.y = e1
        self.z = e2

    def calc_color(self):
        x = int(255.999 * self.x)
        y = int(255.999 * self.y)
        z = int(255.999 * self.z)
        return f"{x} {y} {z}"

    def __str__(self):
        return f"{self.x} {self.y} {self.z}"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vec3(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vec3(x, y, z)

    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        z = self.z * other
        return Vec3(x, y, z)

    def __rmul__(self, other):
        x = self.x * other
        y = self.y * other
        z = self.z * other
        return Vec3(x, y, z)

    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        z = self.z / other
        return Vec3(x, y, z)

    def length(self):
        return sqrt(self.length_squared())

    def length_squared(self):
        return (self.x * self.x) + (self.y * self.y) + (self.z * self.z)


# static methods

def unit_vector(v: Vec3) -> Vec3:
    return v / v.length()


def dot(v1: Vec3, v2: Vec3) -> float:
    return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z


def cross(v1: Vec3, v2: Vec3) -> Vec3:
    a = (v1.y * v2.z) - (v1.z * v2.y)
    b = (-v1.x * v2.z) - (v1.z * v2.x)
    c = (v1.x * v2.y) - (v1.y * v2.x)
    return Vec3(a, b, c)