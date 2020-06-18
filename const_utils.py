from math import inf
from random import randint, randrange, uniform


infinity = inf
pi = 3.1415926535897932385


def degrees_to_radians(degrees: float) -> float:
    return degrees * pi / 180.0


def random_int() -> int:
    return randint(0, 1)


def random_float(min_n: float = 0.0, max_n: float = 1.0) -> float:
    return uniform(min_n, max_n)


def clamp(x: float, min: float, max: float) -> float:
    if x < min:
        return min

    if x > max:
        return max

    return x
