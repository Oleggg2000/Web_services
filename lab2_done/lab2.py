import numpy as np
import matplotlib.pyplot as plt
from math import fabs
from PIL import Image, ImageDraw


import lab2_2
import lab2_3


def resize_image(input_image_path, output_image_path, size_):
    try:
        original_image = Image.open(input_image_path)
    except FileNotFoundError:
        print("File is not found")
    resized_image = original_image.resize(size_)    #Resizing image to custom size
    resized_image.show()
    original_image.thumbnail((400, 200))
    original_image.show()
    original_image.save("images/mustang_resized_2.jpg")
    resized_image.save(output_image_path)


def gold_left_corner(input_image_path, output_image_path, rec_width, rec_height):
    try:
       my_image = Image.open(input_image_path)
    except FileNotFoundError:
        print("File is not found")
    pixels = my_image.load()
    height, width = my_image.size
    for i in range(rec_height):
        for j in range(width-rec_width, width):
            my_image.putpixel((i, j), (255, 215, 0))
    my_image.show()
    my_image.save(output_image_path)


def red_shade_image(input_image_path, output_image_path):
    try:
        image_=Image.open(input_image_path)
    except FileNotFoundError:
        print("File is not found")
    #r, g, b = image_.split()
    data = image_.getdata()
    r = [(d[0], 0, 0) for d in data]
    g = [(0, d[1], 0) for d in data]
    b = [(0, 0, d[2]) for d in data]
    image_.putdata(r)
    image_.show()
    image_.save(output_image_path)


def gradient(input_image_path, output_image_path, rec_width, rec_height):
    try:
        new_image = Image.open(input_image_path)
    except FileNotFoundError:
        print("File is not found")
    x_dif = 0
    draw = ImageDraw.Draw(new_image)
    width, height = new_image.size
    pixels = new_image.load()
    for x in range(0, width//255*255, width//255):
        for y in range(rec_height):
            for k in range(width//255):
                draw.point((x+k, y), (0, 0+x_dif, 0))
        if x_dif <= 255:
            x_dif += 1

    new_image.show()
    new_image.save(output_image_path)


gradient("images/source/mustang.jpg", "images/mustang_with_gradient.jpg", 500, 200)
red_shade_image("images/source/mustang.jpg", "images/mustang_red_shade.jpg")
gold_left_corner("images/source/mustang.jpg", "images/mustang_gold_corner.jpg", 200, 200)
resize_image("images/source/mustang.jpg", "images/mustang_resized.jpg", (1080, 920))

# Using another image
# gradient("images/source/camaroSS.jpg", "images/mustang5.jpg", 500, 200)
# red_shade_image("images/source/camaroSS.jpg", "images/mustang4.jpg")
# gold_left_corner("images/source/camaroSS.jpg", "images/mustang3.jpg", 200, 200)
# resize_image("images/source/camaroSS.jpg", "images/mustang2.jpg", (1080, 920))

# From lab2_3.py Some kind of changes with image
lab2_3.im_changes()
# From lab2_2.py Images with gauss and poisson noise
lab2_2.noisy()