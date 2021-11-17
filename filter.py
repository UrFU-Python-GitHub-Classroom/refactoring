from PIL import Image
import numpy as np


def pixel_brightness(arr, b_s, gr, i, j):
    brightness = np.sum(arr[i: i + b_s, j: j + b_s]) // (b_s * b_s * 3)
    brightness -= brightness % gr
    return brightness


def transform_to_mosaic(arr, b_s, gr):
    for i in range(0, len(arr), b_s):
        for j in range(0, len(arr[1]), b_s):
            brightness = pixel_brightness(arr, b_s, gr, i, j)
            arr[i: i + b_s, j: j + b_s] = np.full(3, brightness)


def convert_image_to_mosaic(img_in="img2.jpg", img_out="res.jpg", block_size=10, gradation_step=50):
    img = Image.open(img_in)
    img_arr = np.array(img)
    transform_to_mosaic(img_arr, block_size, gradation_step)
    res = Image.fromarray(img_arr)
    res.save(img_out)

convert_image_to_mosaic()