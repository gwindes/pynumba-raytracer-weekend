from hittable import Hittable, HitRecord
from ray import Ray


class HittableList(Hittable):

    def __init__(self):
        self.list = list()

    def add(self, object: Hittable) -> None:
        self.list.append(object)

    def clear(self):
        self.list = list()

    def hit(self, ray: Ray, t_min: float, t_max: float, hit_record: HitRecord) -> bool:
        temp_record = HitRecord()
        hit_anything = False
        closest_so_far = t_max

        for scene_object in self.list:
            if scene_object.hit(ray, t_min, closest_so_far, temp_record):
                hit_anything = True
                closest_so_far = temp_record.t

                hit_record.t = temp_record.t
                hit_record.normal = temp_record.normal
                hit_record.front_face = temp_record.front_face
                hit_record.point = temp_record.point

        return hit_anything
