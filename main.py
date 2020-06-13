

def main():
    image_width = 256
    image_height = 256

    print(f"P3\n{image_width} {image_height}\n255")

    for y in range(image_height-1, 0, -1):
        for x in range(image_width):
            r = y / (image_width-1)
            g = x / (image_height-1)
            b = 0.25

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            print(f"{ir} {ig} {ib}")


main()