import PIL
from PIL import Image

file = 'binance.jpeg'
image = Image.open(file)

print('{}x{}'.format(image.width, image.height))

from PIL import ImageDraw

drawing_object = ImageDraw.Draw(image)
drawing_object.rectangle((0, 1050, 792, 1410), fill=None, outline='red')
image.show()
