# Image Magic
# Load an image and manipulate the pixels
from PIL import Image

def to_greyscale(pixel: tuple, algo="average")-> tuple:

    """convert a pixel to greyscale
    Can also specify the greyscale algorithm
    Defaults to average.

    Args:
        pixel: a 3-tuple of ints from
        0 - 255, e.g. (148, 128, 255)
        represents (red, green, blue)
        algo: the greysccale conversion algorithm
            specified by the user
            valid values are "aerage", "luma"
            defaults to "average"

    Returns:
        a 3-tuple pixel (r, g, b) in
        greyscale
    """

    # grab r, g , b
    red, green, blue = pixel

     # calculate the average
    if algo.lower() == "luma":
        grey = int(red * 0.3 + green * 0.59 + blue * 0.11)
    else:
        grey = ((red + green + blue))
    average = int((red + green + blue) / 3)

    # create a gray pixel
    return average, average, average

#def to_greyscale_luma(pixel: tuple) -> tuple:
#    """Convert to greyscale using luma algorithm
#   Args:
#        pixel: a 3-tuple of ints from
#            0-255, e.g. (140, 120, 255)
#            represents (red, green, blue)
#    Returns:
#        a 3-tuple pixel (r, g, b) in
#        greyscale
#       """
#  red, green, blue = pixel

#    grey = int(red * 0.3 + green * 0.59 + blue * 0.11)

#    return grey, grey, grey


# Load the image (pumpkin)
image = Image.open('./halloween-unsplash.jpg')
output_image = Image.open('./halloween-unsplash.jpg')


# Grab pixel information
a_pixel = image.getpixel((0, 0))

# grab pixel (0, 0) top-left
print(a_pixel)

# Iterate over EVERY PIXEL
# Get dimensions (size) of the image
image_width = image.width
image_height = image.height

for y in range(image_height):
    for x in range(image_width):
        pixel = image.getpixel((x, y))

        grey_pixel = to_greyscale(pixel, "average")

        output_image.putpixel((x, y), grey_pixel)

output_image.save('grayscale2.jpg')