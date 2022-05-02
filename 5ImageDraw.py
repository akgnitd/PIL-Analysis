import PIL
from PIL import Image

file = 'binance.jpeg'
image = Image.open(file)

# To Apply the Filters, we need to convert the image to RGB mode
image = image.convert('RGB')
print('{}x{}'.format(image.width, image.height))

from PIL import ImageDraw

drawing_object = ImageDraw.Draw(image)
drawing_object.rectangle((0, 1050, 792, 1410), fill=None, outline='red')
image.show()
