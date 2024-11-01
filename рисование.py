# import turtle
# turtle.setup(500, 500)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
#
# turtle.mainloop()


# import turtle
# turtle.setup(500,500)
# turtle.speed(10)
# for i in range(36):
#     for k in range(6):
#         turtle.forward(50)
#         turtle.left(60)
#     turtle.left(10)
#
# turtle.mainloop()


# import turtle
# turtle.setup(500, 500)
# turtle.speed(10)
# for i in range(4):
#     turtle.forward(50)
#     turtle.left(90)
# for k in range(25):
#     turtle.forward(1)
#     turtle.left(90)
#     turtle.forward(50)
#     turtle.right(90)
#     turtle.forward(1)
#     turtle.right(90)
#     turtle.forward(50)
#     turtle.left(90)
#
# turtle.mainloop()

import random
import turtle

allColor = []
while True:
    color = input()
    if color == 'exit':
        break
    else:
        allColor.append(color)

turtle.setup(500, 500)

x = - 250
y = -250

for j in range(10):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    random.choice(allColor)

    x += 55
    y += 55

    for i in range(4):
        turtle.forward(50)
        turtle.left(90)



turtle.mainloop()


