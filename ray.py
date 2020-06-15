from vec3 import Vec3


class Ray(object):

    def __init__(self, origin: Vec3, direction: Vec3):
        self.origin = origin
        self.direction = direction

    def at(self, t: float) -> Vec3:
        return self.origin + t*self.direction

