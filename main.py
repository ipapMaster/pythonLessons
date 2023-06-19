import turtle as t

colors = ['red', 'purple', 'blue', 'green',
          'yellow', 'orange', 'cyan', 'magenta', 'pink']
t.bgcolor('black')
t.speed(0)  # мгновенная скорость
angle = 39  # нестандартный поворот :)
for x in range(200):
    t.pencolor(colors[x % 9])
    t.width(x // 100 + 1)
    t.forward(x)
    t.left(angle)

t.mainloop()
