from camera import Camera
from hittable import HitRecord, Hittable
from hittable_list import HittableList
from sphere import Sphere
from vec3 import *
from ray import Ray
from math import sqrt
from const_utils import infinity, random_float


def ray_color(ray: Ray, world: Hittable) -> Vec3:
    hit_record = HitRecord()
    if world.hit(ray, 0, infinity, hit_record):
        return 0.5 * (hit_record.normal + Vec3(1, 1, 1))

    unit_direction = Vec3(unit_vector(ray.direction))

    t = 0.5 * (unit_direction.y + 1.0)
    return (1.0-t) * Vec3(1.0, 1.0, 1.0) + t * Vec3(0.5, 0.7, 1.0)


def hit_sphere(center: Vec3, radius: float, ray: Ray) -> float:
    oc = ray.origin - center
    a = ray.direction.length_squared(2.0) #dot(ray.direction, ray.direction)
    half_b = dot(oc, ray.direction)
    c = oc.length_squared() - radius*radius
    discriminant = half_b*half_b - a*c

    if discriminant < 0:
        return -1.0

    return (-half_b - sqrt(discriminant)) / float(a)


def main():
    aspect_ratio = 16.0 / 9.0
    image_width = 1280
    image_height = int(image_width / aspect_ratio)

    samples_per_pixel = 4

    print(f"P3\n{image_width} {image_height}\n255")

    world = HittableList()
    world.add(Sphere(Vec3(0, 0, -1), 0.5))
    world.add(Sphere(Vec3(0, -100.5, -1), 100))

    camera = Camera()

    for y in range(image_height-1, 0, -1):
        for x in range(image_width):
            pixel_color = Vec3()
            for i in range(samples_per_pixel):
                nx = float(image_width)
                ny = float(image_height)
                u = float(x + random_float()) / nx
                v = float(y + random_float()) / ny

                ray = camera.get_ray(u, v)
                pixel_color += ray_color(ray, world)

            pixel_color /= samples_per_pixel
            print(pixel_color.calc_color())


main()

