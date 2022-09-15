from turtle import *
from freegames import vector
from math import sqrt

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y) #The pointer starts on the first point that the/
    #player clicks on
    begin_fill()

    goto(end.x, end.y) #The pointer goes to the second point the player/
    #clicks on to simulate the circle's radius
    left(90) #The cursor faces 90 degrees to the left in order to start the/
    #circunference

    down()
    for count in range(360): #The method starts counting the degrees, going/
        #from 0 to 360 in order to draw the circle
        forward(0.017*sqrt(((end.x-start.x)**2)+((end.y-start.y)**2))) #The/
        #cursor moves forward the length of the radius times 1 degree in/
        #radians, following the formula for calculating the arc length.
        left(1) #The cursor moves one degree to the left

    right(90) #The cursor resets it's initial orientation
    end_fill()

def rectangle(start, end):
    "Draw rectangle from start to end"
    up()
    goto(start.x,start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward((end.x - start.x)*2) #Draws the height of the rectangle as double of its width
        left(90)

    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x,start.y)
    down()
    begin_fill()
    
    for count in range(2): #Draws the first line and the second one of the triangle
        forward(end.x - start.x)
        left(120) #Turns 120 degrees for the second line


    end_fill()
    left(120) #Resets the cursor to the default position

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('orange'), 'O') #The color added to the game is orange/
#which can be accessed by the player by typing 'O' on the keyboard.
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
