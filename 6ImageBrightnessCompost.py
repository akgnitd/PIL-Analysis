import PIL
from PIL import Image

file = 'binance.jpeg'
image = Image.open(file)

print('{}x{}'.format(image.width, image.height))

# Changing the brigthness of the image and compositing them one above another in a contact sheet
from PIL import ImageEnhance

enhancer = ImageEnhance.Color(image)
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
