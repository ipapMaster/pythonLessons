# PIL - Python Imaging Library
from PIL import Image, ImageDraw, ImageFont

W, H = 600, 400  # зададим ширину и высоту
BLACK = (0, 0, 0)
FGREEN = (34, 139, 34)
ORANGE = (255, 69, 0)

# создали холст
canvas = Image.new('RGB', (W, H), FGREEN)

# создали объект для рисования (на холсте)
draw = ImageDraw.Draw(canvas)

# выберем тип объекта
draw.line((0, 0, W, H), fill=ORANGE, width=5)
draw.line((W, 0, 0, H), fill=ORANGE, width=5)
draw.rectangle((0, 0, W, H), outline=ORANGE, width=5)
draw.ellipse((100, 0, H + 100, H), outline=ORANGE, width=5)
font = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 50)
text = 'PYTHON'
draw.text((200, 150), text, font=font, fill=ORANGE)
draw.polygon((W // 2, 0, 0, H, W, H),
             outline=ORANGE, width=5)

canvas.save('canvas_line.png')
