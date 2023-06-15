import turtle as t

dist = 200
sides = 6
angle = 360 / sides

t.shape('turtle')  # задаём форму черепахи

t.forward(dist)  # magic value
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)

t.mainloop()  # ожидание действий пользователя
