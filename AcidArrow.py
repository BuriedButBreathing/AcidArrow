# AcidArrow V0.1
# Written by Chris Higgins
# Requires PyPillow to function
from PIL import Image as Im

'''
NOTES
https://imgur.com/a/DFKFCel URL for PNG file
https://imgur.com/a/b6UvuqO URL for the BMP file
using BMP eliminates the need to remove alpha channel values
Use RequestLibrary for HTTP requests
Convert this to use functions where possible
Tuple with functions?
'''

'''
This section imports an image from the directory the script lives in,
gathers the values of the individual pixels, and prints out the file type,
dimensions, encoding, and then the pixel values as individual arrays.
'''

try:
    codex = Im.open('test.bmp')
    pixelvalues = list(codex.getdata())
    del pixelvalues[19]
    del pixelvalues[18]
    print(sep="\n", *pixelvalues)
    print('Parsing Okay')
    # Splits tuples into individual integers
    for values in pixelvalues:
        for single_value in values:
            append = "[char]"
            str(single_value)
            print(append + single_value)
            # result = append + single_value
            # print(result)
            continue


# This section is for error handling

except:
    print("Something bad happened and we crashed")
