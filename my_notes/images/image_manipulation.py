'''             IMAGE MANIPULATION
Convert an image to grayscale.
Convert an image to another data type.
Resize an image.
Rotate an image.




'''
# load and show an image with Pillow
from turtle import clear
import pillow

# Load the image
img = Image.open('pup_images/tan.jpeg') .convert('L')

# Get basic details about the image
# print(img.format)  # JPEG
# print(img.mode)  # RGB
# print(img.size)  # (290, 193)

# Show image
img.show()

#  save image
img.save("puppies/tan1_gs.jpeg")

