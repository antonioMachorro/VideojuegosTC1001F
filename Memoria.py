from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
clicks = 0

# Array of 32 colors for each number
colors=['cornflower blue','blue','navy','light blue','powder blue','steel blue','cyan',
'dark turquoise','teal','aquamarine','medium sea green','pale green','lime green','green',
'green yellow','yellow green','dark khaki','yellow','peru','orange','firebrick','maroon','coral',
'red','salmon','indian red','deep pink','deep pink','medium violet red','magenta','dark violet', 'medium slate blue']

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    global clicks #Declares the previously established variable clicks as a/
    #global variable in order to use it in this method
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        clicks = clicks + 1 #Adds 1 to the global amount of clicks per tap
        print('Taps:', clicks) #Prints the number of clicks on-screen
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    restantes = 0 #Creates a variable that counts how many remaining squares/
    #are unsolved on the board
    
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
            restantes = restantes + 1 #Adds a remaining unsolved square per/
            #hidden squares in the array

    if restantes ==  0: #Checks if there are no remaining unsolved squares
        print('Se ha descubierto toda la imagen.') #Prints a message once all/
        #squares have been solved
        return 

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        if tiles[mark] < 10: # Centers the number if its one digit
            goto(x + 15, y)
        else:
            goto(x + 4, y) 
        color(colors[tiles[mark]]) # Uses the colors of the list for each number
        write(tiles[mark], font=('Arial', 30, 'normal'))
    
    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
