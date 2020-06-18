from ray import Ray
from vec3 import Vec3, dot


class HitRecord(object):

    def __init__(self, point=Vec3(), normal=Vec3(), t=0.0):
        self.point = point
        self.normal = normal
        self.t = t
        self.front_face = None

    def set_face_normal(self, ray: Ray, outward_normal: Vec3) -> None:
        self.front_face = dot(ray.direction, outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal


class Hittable(object):

    def hit(self, ray: Ray, t_min: float, t_max: float, hit_record: HitRecord) -> bool:
        raise Exception('Must be implemented in class')
