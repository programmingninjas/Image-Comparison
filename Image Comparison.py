from PIL import Image,ImageChops
from image_tools.sizes import resize_and_crop

def get_black_pixels(image):
    black_and_white_version = image.convert('1')
    black_pixels = black_and_white_version.histogram()[0]
    return black_pixels

def img_comp(current, expected):

        diff = ImageChops.difference(current, expected)
        black_pixels = get_black_pixels(diff)
        total_pixels = diff.size[0] * diff.size[1]
        similarity_ratio = black_pixels / total_pixels
        result = (1 - similarity_ratio) * 100
        print('The images are different by {}%'.format(result))
        return result

image1 = Image.open(input("Enter Image1 Path: ") )
image2 = Image.open(input("Enter Image2 Path: ") )

img_comp(image1,image2)
