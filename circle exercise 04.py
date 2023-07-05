import turtle

from itertools import  cycle
colors = cycle({'red','orange','yellow','pink','purple','thistle'})

def draw_shape(size, angle , shift ,shape):

    turtle.pencolor(next(colors))
    next_shape = 'square'
    if shape == 'circle':
        turtle.circle(size)
        next_shape = 'square'
    elif shape == 'square':
        for i in range (4):
            turtle.forward(size+10)
            turtle.left(90)
        next_shape = 'circle'
    turtle.right(angle)
    turtle.forward(shift)
    draw_shape( 10,90,4,'square')

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_shape(40,0,5,'circle')


    
