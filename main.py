import turtle as t

dist = 60
figs = 12
FS = 8  # число сторон фигуры
f_angle = 360 / FS  # угол фигуры
angle = 360 / figs
f_counter = 0  # счётчик фигур

t.shape('turtle')  # задаём форму черепахи

while f_counter < figs:
    s_counter = 0
    while s_counter < FS:
        t.forward(dist)
        t.left(f_angle)
        s_counter += 1
    t.right(angle)
    f_counter += 1

t.mainloop()  # ожидание действий пользователя
