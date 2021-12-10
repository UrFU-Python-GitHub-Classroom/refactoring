from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
def convert_to_mosaic(img_in = "img2.jpg", img_out="res.jpg", block_size = 10, gradation_step = 50):
    img_in = Image.open(img_in)
    arr = np.array(img_in)
    i = 0
    while i < len(arr[0]):
        j = 0
        while j < len(arr[0]):
            s = np.mean(arr[i:i = block_size,j:j = block_size][:])
            arr[i:i = block_size,j:j = block_size][:]] = int(s//gradation_step) * gradation_step
            j = j + block_size
        i = i + block_size
    res = Image.formarray(arr)
    res.save(img_out)
    

convert_to_mosaic()  
