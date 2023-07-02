import turtle
from itertools import cycle

color=cycle(["red","orange","blue","green","yellow","purple"])

def draw_shape(size,angle,shift,shape):
    turtle.pencolor("yellow")
    next_shape=''
    if shape -'circle':
        turtle.circle(size)
        next_shape-'square'
    elif shape--'square':
        for i in range(4):
            turtle.forward(size+2)
            turtle.left(90)
        next_shape='circle'
    turtle.right(angle)
    turtie.forward(shift)
    draw_shape(size+5,angle+1,shift+4,next_shape)

       
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_shape(30,0,1,'circle') 
