import PIL
from PIL import Image

file = 'binance.jpeg'
image = Image.open(file)

print(PIL.__version__)
print(image)

print('** Print Image type **')
print(str(type(image)))

print('** Import Inspect **')
import inspect

print(inspect.getmro(type(image)))

print('** Showing Image **')
# image.show()

from IPython.display import display

print('** Displaying Image **')
display(image)

print('** Saving Image As a New File **')
image.save("binanceAs.png")
image2 = Image.open("binanceAs.png")

print('** Comparing Image Type **')
print(inspect.getmro(type(image)))
print(inspect.getmro(type(image2)))

from PIL import ImageFilter

print('** Applying Filters To Image **')
# To Apply the Filters, we need to convert the image to RGB mode
image = image.convert('RGB')

print('** Added Blurred Filter **')
blur_image = image.filter(PIL.ImageFilter.BLUR)
display(blur_image)
image.save('blur_image.png')
print('** Showing Blurred Image **')
# blur_image.show()

print('** Added Sharpen Filter **')
sharpen_image = image.filter(PIL.ImageFilter.SHARPEN)
print('** Showing Sharpen Image **')
# sharpen_image.show()

print('** Added Emboss Filter **')
emboss_image = image.filter(PIL.ImageFilter.EMBOSS)
print('** Showing Emboss Image **')
# emboss_image.show()

print('** Added Smooth Filter **')
smooth_image = image.filter(PIL.ImageFilter.SMOOTH)
print('** Showing Smooth Image **')
# smooth_image.show()

print('** Added Find Edges Filter **')
find_edges_image = image.filter(PIL.ImageFilter.FIND_EDGES)
print('** Showing  Find Edges Image **')
# find_edges_image.show()

print('{}x{}'.format(image.width, image.height))

print('** Cropping Image (left, upper, right, lower) **')
cropped_image = image.crop((0, 1050, 792, 1410))
# cropped_image.show()

from PIL import ImageDraw

drawing_object = ImageDraw.Draw(image)
drawing_object.rectangle((0, 1050, 792, 1410), fill=None, outline='red')
# image.show()

# Changing the brigthness of the image and compositing them one above another in a contact sheet
from PIL import ImageEnhance

enhancer = ImageEnhance.Brightness(image)
images = []

for i in range(0, 10):
    images.append(enhancer.enhance(i / 10))

print(images)

first_image = images[0]
# contact_sheet creation
contact_sheet = Image.new(first_image.mode, (first_image.width * 10, first_image.height))

# contact_sheet.show()  # This is a black image with size 10 times width of our image and same height

# Adding all the Images in the contact_sheet in loop. Need to pass the x,y location for each images. Here, we will have y as fixed and x will change for each image
current_location = 0
for img in images:
    contact_sheet.paste(img, (current_location, 0))
    current_location += 792

# contact_sheet.show()
# contact_sheet.resize((1500, 800)).show()


# Making it a 3x3 Image
contact_sheet = Image.new(first_image.mode, (first_image.width * 3, first_image.height * 3))
x = y = 0

for img in images[1:]:
    contact_sheet.paste(img, (x, y))
    if y + first_image.height == contact_sheet.height:
        y = 0
        x += first_image.width
    else:
        y += first_image.height

contact_sheet.show()
