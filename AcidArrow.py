# AcidArrow V0.1
# Written by Chris Higgins
# Requires PyPillow to function
from PIL import Image as Im

'''
NOTES

https://imgur.com/a/DFKFCel URL for PNG file
https://imgur.com/a/b6UvuqO URL for the BMP file
using BMP eliminates the need to remove alpha channel values

'''

'''
This section imports an image from the directory the script lives in,
gathers the values of the individual pixels, and prints out the file type,
dimensions, encoding, and then the pixel values as individual arrays.
'''

try:
    codex = Im.open('test.bmp')
    pixelvalues = list(codex.getdata())
    print('The image is: ')
    print(codex.format, codex.size, codex.mode)
    pixelarray = pixelvalues
    del pixelvalues[18]
    print(sep="\n", *pixelvalues)


# This section is for error handling

except:
    print("Something bad happened and we crashed")

