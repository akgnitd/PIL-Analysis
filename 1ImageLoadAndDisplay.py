import PIL
from PIL import Image

file = 'binance.jpeg'
image = Image.open(file)

print('** Print Image type **')
print(str(type(image)))

print('** Import Inspect **')
import inspect

print(inspect.getmro(type(image)))

print('** Showing Image **')
image.show()

from IPython.display import display

print('** Displaying Image **')
display(image)
