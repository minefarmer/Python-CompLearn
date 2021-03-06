'''                 LOADING AND DISPLAYING IMAGES
How to load an image and also interact with the image and retrivingsome details from that image during the interaction with the image, we are going to display information about the format.
Get information about image mode.
Get information about image size.
Display the image




'''
# load and show an image with Pillow
from PIL import Image

# Load the image
img = Image.open('pup_images/tan.jpeg')

# Get basic details about the image
print(img.format)  # JPEG
print(img.mode)  # RGB
print(img.size)  # (290, 193)

# Show image
img.show()

#  save image
img.save('pup_images/puppy1_gs.jpeg')

# image resize
img = Image.open('pup_images/puppy1_gs.jpeg')

newImage = img.resize((450,500))

newImage.save('pup_images/puppy1resized.jpeg')

img.rotate(45).show()

