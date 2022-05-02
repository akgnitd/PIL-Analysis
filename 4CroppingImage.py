import PIL
from PIL import Image

file = 'binance.jpeg'
image = Image.open(file)

print('{}x{}'.format(image.width, image.height))

print('** Cropping Image (left, upper, right, lower) **')
cropped_image = image.crop((0, 1050, 792, 1410))
cropped_image.show()
