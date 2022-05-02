import PIL
from PIL import Image

file = 'binance.jpeg'
image = Image.open(file)

from PIL import ImageFilter

print('** Applying Filters To Image **')
# To Apply the Filters, we need to convert the image to RGB mode
image = image.convert('RGB')

print('** Added Blurred Filter **')
blur_image = image.filter(PIL.ImageFilter.BLUR)
display(blur_image)
image.save('blur_image.png')
print('** Showing Blurred Image **')
blur_image.show()

print('** Added Sharpen Filter **')
sharpen_image = image.filter(PIL.ImageFilter.SHARPEN)
print('** Showing Sharpen Image **')
sharpen_image.show()

print('** Added Emboss Filter **')
emboss_image = image.filter(PIL.ImageFilter.EMBOSS)
print('** Showing Emboss Image **')
emboss_image.show()

print('** Added Smooth Filter **')
smooth_image = image.filter(PIL.ImageFilter.SMOOTH)
print('** Showing Smooth Image **')
smooth_image.show()

print('** Added Find Edges Filter **')
find_edges_image = image.filter(PIL.ImageFilter.FIND_EDGES)
print('** Showing  Find Edges Image **')
find_edges_image.show()
