import PIL
from PIL import Image

file = 'binance.jpeg'
image = Image.open(file)

print(PIL.__version__)
print(image)

print('** Print Image type **')
print (str(type(image)))

print('** Import Inspect **')
import inspect
print(inspect.getmro(type(image)))

print('** Showing Image **')
image.show()

from IPython.display import display
print('** Displaying Image **')
display(image)

print('** Saving Image As a New File **')
image.save("binanceAs.png")
image2 = Image.open("binanceAs.png")

print('** Comparing Image Type **')
print (inspect.getmro(type(image)))
print (inspect.getmro(type(image2)))

from PIL import ImageFilter
print('** Applying Filters To Image **')
#To Apply the Filters, we need to convert the image to RGB mode
image=image.convert('RGB')
blur_image = image.filter(PIL.ImageFilter.BLUR)
display(blur_image)
image.save('blur_image.png')

print('** Showing Blurred Image **')
blur_image.show()
