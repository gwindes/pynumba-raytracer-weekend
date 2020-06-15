from vec3 import *
from ray import Ray
from math import sqrt


def ray_color(ray: Ray) -> Vec3:
    t = hit_sphere(Vec3(0.0, 0.0, -1.0), 0.5, ray)

    if t > 0.0:
        n = unit_vector(ray.at(t) - Vec3(0, 0, -1))
        return 0.5 * Vec3(n.x+1, n.y+1, n.z+1)

    unit_direction = Vec3(unit_vector(ray.direction))
    t = 0.5 * (unit_direction.y + 1.0)
    return (1.0-t) * Vec3(1.0, 1.0, 1.0) + t * Vec3(0.5, 0.7, 1.0)


def hit_sphere(center: Vec3, radius: float, ray: Ray) -> float:
    oc = ray.origin - center
    a = ray.direction.length_squared() #dot(ray.direction, ray.direction)
    half_b = dot(oc, ray.direction)
    c = oc.length_squared() - radius*radius
    discriminant = half_b*half_b - a*c

    if discriminant < 0:
        return -1.0

    return (-half_b - sqrt(discriminant)) / float(a)


def main():
    image_width = 400
    image_height = 200
    focal_length = 1.0
    aspect_ratio = float(image_width) / float(image_height)

    origin = Vec3(0.0, 0.0, 0.0)
    horizontal = Vec3(4.0, 0.0, 0.0)
    vertical = Vec3(0.0, 2.0, 0.0)
    lower_left_corner = origin - horizontal/2.0 - vertical/2.0 - Vec3(0.0, 0.0, focal_length)

    print(f"P3\n{image_width} {image_height}\n255")

    for y in range(image_height-1, 0, -1):
        for x in range(image_width):
            nx = float(image_width)
            ny = float(image_height)
            u = float(x) / nx
            v = float(y) / ny

            ray = Ray(origin, lower_left_corner + u*horizontal + v*vertical - origin)
            pixel_color = ray_color(ray)

            print(pixel_color.calc_color())


main()

