import turtle
import time

threshold = 5
ratio = 0.5
startDistance = 300
turtle.screensize(6000,6000)
turtle.speed(1000)

def left(distance):
    time.sleep(0.100)
    if (distance > threshold):
        turtle.forward(distance)
        right(distance*ratio)
        turtle.forward(distance)
        right(distance*ratio)
        turtle.forward(distance)
        right(distance*ratio)
    else:
        turtle.forward(distance-distance*ratio*ratio)
        turtle.right(90)
        turtle.forward(distance-distance*ratio*ratio)
        turtle.right(90)
        turtle.forward(distance-distance*ratio*ratio)
        turtle.right(90)

def right(distance):
    time.sleep(0.100)
    if (distance > threshold):
        turtle.forward(distance)
        left(distance*ratio)
        turtle.forward(distance)
        left(distance*ratio)
        turtle.forward(distance)
        left(distance*ratio)
    else:
        turtle.forward(distance-distance*ratio*ratio)
        turtle.left(90)
        turtle.forward(distance-distance*ratio*ratio)
        turtle.left(90)
        turtle.forward(distance-distance*ratio*ratio)
        turtle.left(90)


for i in range(4):
    right(startDistance)
    turtle.forward(startDistance/ratio)
turtle.done()
