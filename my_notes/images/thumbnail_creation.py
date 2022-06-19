'''                 WHAT IS A THUMBNAIL?

A thumbnail is a compressed preview image of the original that is used as aplaceholder.






'''
# Load and show an image with pillow.
from PIL import Image
import glob, os  # os module allows Python to interact with my operating system.

size = 128, 128

for infile in glob.glob("pup_images/*jpeg"):
    file, ext = os.path.splitext(infile)
    img = Image.open(infile)
    img.thumbnail(size,Image.ANTIALIAS)  # ANTIALIAS: Minimizes the distortion when representing a high resolution image at a lower resolution.
    img.save(file + ".thumbnail", "JPEG")  # file not displayed because VSC could not read.  # unnown file type.

