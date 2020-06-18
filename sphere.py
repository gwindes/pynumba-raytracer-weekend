from math import sqrt

from hittable import Hittable, HitRecord
from ray import Ray
from vec3 import Vec3, dot


class Sphere(Hittable):

    def __init__(self, center: Vec3, radius: float):
        self.center = center
        self.radius = radius

    def hit(self, ray: Ray, t_min: float, t_max: float, hit_record: HitRecord) -> bool:
        oc = ray.origin - self.center
        a = ray.direction.length_squared()  # dot(ray.direction, ray.direction)
        half_b = dot(oc, ray.direction)
        c = oc.length_squared() - self.radius * self.radius
        discriminant = half_b * half_b - a * c

        if discriminant > 0:
            root = sqrt(discriminant)
            temp = (-half_b - root) / a

            if t_max > temp > t_min:
                hit_record.t = temp
                hit_record.point = ray.at(temp)
                outward_normal = (hit_record.point - self.center) / self.radius
                hit_record.set_face_normal(ray, outward_normal)
                return True

            temp = (-half_b + root) / a
            if t_max > temp > t_min:
                hit_record.t = temp
                hit_record.point = ray.at(temp)
                outward_normal = (hit_record.point - self.center) / self.radius
                hit_record.set_face_normal(ray, outward_normal)
                return True

        return False

