# PIL - Python Imaging Library
from PIL import Image, ImageFilter

original = Image.open('python.png')

contour = original.filter(ImageFilter.CONTOUR)

contour.save('contour.png')