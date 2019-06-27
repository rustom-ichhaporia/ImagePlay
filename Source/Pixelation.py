import numpy as np
import matplotlib
from PIL import Image, ImageFilter

# Base and iterated image can be converted into arguments.
# Scaling and opacity constants can be changed as well.

scaling_constant = 40
opacity_constant = 0.8

base = Image.open("Images/Inputs/Landscape_1.jpg")
base.show()
iterated_image = Image.open("Images/Inputs/Rustom2.jpg")

small_x, small_y = (iterated_image.size[0] // scaling_constant, iterated_image.size[1] // scaling_constant)

module = iterated_image.resize((small_x, small_y))

base_image_small = base.resize((base.size[0] // small_x, base.size[1] // small_y))
pixels = base_image_small.load()

final = Image.new("RGB", base.size)
for x in range(base_image_small.size[0]):
    for y in range(base_image_small.size[1]):
        color_block = Image.new("RGB", module.size, pixels[x, y])
        tinted_module = Image.blend(module, color_block, opacity_constant)
        final.paste(tinted_module, (x*small_x, y*small_y))
final.show()

final.save("Images/Outputs/ImagePixelationOutput.png", "PNG")
