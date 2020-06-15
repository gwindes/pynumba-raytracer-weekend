from vec3 import *
from ray import Ray


def ray_color(ray: Ray) -> Vec3:
    bhit_sphere = hit_sphere(Vec3(0.0, 0.0, -1.0), 0.5, ray)
    if bhit_sphere:
        return Vec3(1, 0, 0)
    unit_direction = Vec3(unit_vector(ray.direction))
    t = 0.5 * (unit_direction.y + 1.0)
    return (1.0-t) * Vec3(1.0, 1.0, 1.0) + t * Vec3(0.5, 0.7, 1.0)


def hit_sphere(center: Vec3, radius: float, ray: Ray) -> bool:
    oc = ray.origin - center
    a = dot(ray.direction, ray.direction)
    b = 2.0 * dot(oc, ray.direction)
    c = dot(oc, oc) - radius*radius
    discriminant = b*b - 4*a*c
    return discriminant > 0


def main():
    image_width = 800
    image_height = 400
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

