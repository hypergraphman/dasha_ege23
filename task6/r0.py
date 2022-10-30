from turtle import *

speed(0.0001)
cell = 50
left(90)


for _ in range(7):
    forward(10 * cell)
    right(120)

penup()
for x in range(10):
    for y in range(10):
        goto(x * cell, y * cell)
        dot(3, 'red')

done()
