# PIL - Python Imaging Library
from PIL import Image

BLACK = (0, 0, 0)

image = Image.open('python.png')
w, h = image.size  # получим ширину и высоту
pixels = image.load()  # загружаю список пикселей

for i in range(w):
    for j in range(h):
        r, g, b = pixels[i, j]
        pixels[i, j] = g, b, r

image.save('inverted.png')

