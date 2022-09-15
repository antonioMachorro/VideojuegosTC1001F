from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def color(): # Chooses one of 5 colors for the snake and the food
    i=randrange(1,5)
    if i==1:
        return 'blue'
    if i==2:
        return 'pink'
    if i==3:
        return 'orange'
    if i==4:
        return 'green'
    if i==5:
        return 'purple'

color_snake=color()
color_food=color()

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color_snake)

    direccion = randrange(1,5) #A random number between 1 and 4 is selected/
    #to determine the direction in which the food will move.
    #1-right  2-left  3-up  4-down
    if(direccion == 1 and food.x+10 < 190): #Checks the random number, as well/
        #as whether the food will remain inside the screen or not
        food.x = food.x + 10 #Moves the food's coordinates ten points to the/
        #right
        square(food.x, food.y, 9, color_food) #The food moves to the position/
        #obtained in the previous lines
    elif(direccion == 2 and food.x-10 > -200):
        food.x = food.x - 10
        square(food.x, food.y, 9, color_food)
    elif(direccion == 3 and food.y+10 < 190):
        food.y = food.y + 10
        square(food.x, food.y, 9, color_food)
    elif(direccion == 4 and food.y-10 > -200):
        food.y = food.y - 10
        square(food.x, food.y, 9, color_food)
    else:
        square(food.x, food.y, 9, color_food) #If it were to go outside the/
        #scree, the food remains in its current position
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
