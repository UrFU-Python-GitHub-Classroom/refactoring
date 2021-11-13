from PIL import Image
from PIL import ImageChops


def test_1_1():
    """1 этап Верно без функций и параметров"""
    import filter

    result = Image.open("res.jpg")
    correct = Image.open("tests/out/1out.jpg")

    diff = ImageChops.difference(correct, result)
    assert not diff.getbbox()
