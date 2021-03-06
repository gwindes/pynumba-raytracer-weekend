from ray import Ray
from vec3 import Vec3


class Camera(object):

    def __init__(self):
        aspect_ratio = 16.0 / 9.0
        viewport_height = 2.0
        viewport_width = aspect_ratio * viewport_height
        focal_length = 1.0

        self.origin = Vec3(0.0, 0.0, 0.0)
        self.horizontal = Vec3(viewport_width, 0.0, 0.0)
        self.vertical = Vec3(0.0, viewport_height, 0.0)
        self.lower_left_corner = self.origin - self.horizontal / 2.0 - self.vertical / 2.0 - Vec3(0.0, 0.0, focal_length)

    def get_ray(self, u: float, v: float) -> Ray:
        return Ray(
            self.origin,
            self.lower_left_corner + u*self.horizontal + v*self.vertical - self.origin
        )
