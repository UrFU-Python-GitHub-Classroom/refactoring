from PIL import Image
from PIL import ImageChops

from filter import convert_image_to_mosaic


def test_2_1():
    """
    2 этап Функции + Параметры Аргументы по умолчанию
    gradations_count = 50
    gradation_step = 255 // gradations_count = 5
    def convert_image(img_in="img2.jpg",
                      img_out="res.jpg",
                      block_size=10,
                      gradation_step=5):
        pass TODO реализовать функцию(-ии) в файле filter.py
    """
    convert_image_to_mosaic()

    result = Image.open("res.jpg")
    correct = Image.open("tests/out/1out.jpg")

    diff = ImageChops.difference(correct, result)
    assert not diff.getbbox()


def test_2_2():
    """2 этап Тест 2"""
    convert_image_to_mosaic(img_in="img2.jpg",
                                   img_out="res2.jpg",
                                   block_size=15,
                                   gradation_step=4)

    result = Image.open("res2.jpg")
    correct = Image.open("tests/out/2out.jpg")

    diff = ImageChops.difference(correct, result)
    assert not diff.getbbox()


def test_2_3():
    """2 этап Тест 3"""
    convert_image_to_mosaic(img_in="img2.jpg",
                                   img_out="res3.jpg",
                                   block_size=1,
                                   gradation_step=1)

    result = Image.open("res3.jpg")
    correct = Image.open("tests/out/3out.jpg")

    diff = ImageChops.difference(correct, result)
    assert not diff.getbbox()
