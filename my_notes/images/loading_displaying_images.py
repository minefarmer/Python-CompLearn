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
print(img.format)
print(img.mode)
print(img.size)

# Show image

img.show()
