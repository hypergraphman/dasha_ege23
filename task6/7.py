from turtle import *

speed(0.0001)
cell = 5
left(90)
x = y = 0


def move(a, b):
    global x, y
    x += a
    y += b
    goto(x * cell, y * cell)


for _ in range(15):
    move(10, 10)
    move(3, -6)
    move(-9, 3)

penup()
for x in range(14):
    for y in range(11):
        goto(x * cell, y * cell)
        dot(3, 'red')

done()
