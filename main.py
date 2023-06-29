# PIL - Python Imaging Library
from PIL import Image, ImageFilter

original = Image.open('python.png')

blur = original.filter(ImageFilter.BLUR)
blur.save('blur.png')
blur = original.filter(ImageFilter.BoxBlur(5))
blur.save('boxblur.png')
blur = original.filter(ImageFilter.GaussianBlur(5))
blur.save('gaussblur.png')


