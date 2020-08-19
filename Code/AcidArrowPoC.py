# AcidArrow V0.1
# Written by Chris Higgins
# Requires PyPillow to function
from PIL import Image as Im
import subprocess

'''
https://imgur.com/a/b6UvuqO URL for the BMP file
Use RequestLibrary for HTTP requests
Convert this to use functions where possible
PowerShell Sendkeys
popen
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
    foobar_results = []
    for values in pixelvalues:
        for single_value in values:
            foobar_results.append('[char]{}'.format(single_value))
    foobar_results.pop(53)
    # Prints a list of concatenated strings in the format '[char]<value>'
    # print(sep="\n", *foobar_results)
    # Prints a 'write test' in character codes
    output = ('(' + foobar_results[43] + ',' + foobar_results[38] + ',' + foobar_results[29] + ',' + foobar_results[40] + ','
          + foobar_results[25] + ',' + foobar_results[0] + ',' + foobar_results[28] + ',' + foobar_results[35] + ','
          + foobar_results[39] + ',' + foobar_results[40])
    # print(output)
    c1 = subprocess.Popen('powershell.exe', shell=True)
    # c1.communicate('test')
    # print(c1.communicate())
    # print('returncode:', c1.returncode)
    # # print('Finished')


# This section is for error handling

except:
    print("Something bad happened and we crashed")

