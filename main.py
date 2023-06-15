import turtle as t

dist = 200
sides = 6
angle = 360 / sides
counter = 0

t.shape('turtle')  # задаём форму черепахи

while counter < 6:
    t.forward(dist)
    t.right(angle)
    counter = counter + 1

t.mainloop()  # ожидание действий пользователя
