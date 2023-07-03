import os

path = 'images'
images = []
root = os.getcwd()

if not os.path.isdir(path):
    os.mkdir(path)  # директория

files = os.listdir(root)  # вообще все файлы "корня"

for file in files:
    if os.path.isfile(file) and (file.endswith('.png') or file.endswith('.jpg')):
        images.append(file)

for image in images:
    os.replace(image, path + '/' + image)
