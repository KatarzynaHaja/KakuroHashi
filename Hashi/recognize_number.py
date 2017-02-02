import numpy
import PIL

img = PIL.Image.open("generated_boards/43882.png").convert("L")
imgarr = numpy.array(img)