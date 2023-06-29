# PIL - Python Imaging Library
from PIL import Image, ImageFilter

original = Image.open('python.png')
pixels = original.load()
x, y = original.size

for i in range(x // 2):
    for j in range(y):
        pixels[i, j], pixels[x - i - 1, j] = pixels[x - i - 1, j], pixels[i, j]

original.save('flipped.png')
