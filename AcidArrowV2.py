# AcidArrow V0.1
# Written by Chris Higgins
# Requires PyPillow to function
from PIL import Image as Im

'''
NOTES

https://imgur.com/a/DFKFCel URL for PNG file
https://imgur.com/a/b6UvuqO URL for the BMP file
using BMP eliminates the need to remove alpha channel values
RequestLibrary for HTTP requests
'''

'''
This section imports an image from the directory the script lives in,
gathers the values of the individual pixels, and prints out the file type,
dimensions, encoding, and then the pixel values as individual arrays.
'''

'This section imports an image from the file path to be parsed'


def open_image(filename):
    """
    This gets rgb values  from a file
    Args:
        filename (str): file to open rgb values from
    Return:
        pixelvalues (list): list of tuples containing rgb values
        codex (img): the image being parsed
    """
    codex = Im.open(filename)
    pixelvalues = list(codex.getdata())
    del pixelvalues[19]
    del pixelvalues[18]
    print(sep="\n", *pixelvalues)
    return pixelvalues, codex


print('The image is: ')
print(rgb_values)


if __name__ == '__main__':
    rgb_values = open_image(filename='test.bmp')