## AcidArrow V0.1
## Written by Chris Higgins
## Requires PyPillow to function
from PIL import Image as im
import numpy
from IO import BytesIO




## TODO:-Strip 4th Value (Alpha Channel) from every array (Use For Loop?) -For loop to standaradize arrays as individual variables Append [char] to variables to prepare for concationation


## This section imports an image from the directory the script lives in
## gathers the values of the individual pixels, and prints out the filetype,
## dimensions, encoding, and then the pixel values as individual arrays.

try:
    codex = im.open("https://imgur.com/a/DFKFCel")
    pixelvalues =list(codex.getdata())
    print("The image is: ")
    print(codex.format, codex.size, codex.mode)
    pixelarray = (pixelvalues)
    print(pixelvalues)
    

## This section is for error handling

except:
    print ("Something bad happened and we crashed")
