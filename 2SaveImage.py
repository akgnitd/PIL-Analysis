import PIL
from PIL import Image

file = 'binance.jpeg'
image = Image.open(file)

print('** Saving Image As a New File **')
image.save("binanceNew.png")
