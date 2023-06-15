import turtle as t

dist = 100
sides = 8
angle = 360 / sides
counter = 0

t.shape('turtle')  # задаём форму черепахи

while counter < sides:
    t.forward(dist)
    t.right(angle)
    counter = counter + 1

t.mainloop()  # ожидание действий пользователя
