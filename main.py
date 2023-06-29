# PIL - Python Imaging Library
from PIL import Image, ImageFilter

original = Image.open('python.png')

cropped = original.crop((60, 280, 370, 525))

cropped.save('cropped.png')