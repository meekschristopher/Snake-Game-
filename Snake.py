import turtle 
import time 
import random

delay = 0.1

#Score 
score = 0 
high_score = 0 

#Setup Screen 
wn = turtle.Screen()
wn.title('Snake by Meeks Moves')
wn.bgcolor('black')
wn.setup(height=600, width=600)
wn.tracer(0)

#Snake Head 
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('green')
head.penup()
head.goto(0,0)
head.direction = 'stop'

#Snake Food 
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,200)

segments = []

#Pen 

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score: 0 High Score: 0', align='center', font=('Courier', 24, 'italic'))

#Functions 

def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
       head.direction = 'down'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'        

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')

#Main game loop 
while True:
    wn.update()

    #Check for collision with borders 
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'

        #Hide the segments 
        for segment in segments: 
            segment.goto(1000, 1000)

        #Clear the segments
        segments.clear()    

        #Reset the delay 

        delay = 0.1 
        
        #Reset Score
        score = 0 
        pen.clear()
        pen.write('Score: {}  High Score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'italic'))
        


    #Check for collision with the food 
    if head.distance(food) < 20: 
        #Move the food to a random spot 
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        #Add a segment 
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('triangle')
        new_segment.color('white')
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        
        #Increase the score 
        score += 10 

        if score > high_score:
            high_score = score 

        pen.clear()
        pen.write('Score: {}  High Score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'italic'))     


    #Move the end segments first in reverse order
    for index in range(len(segments) -1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segement 0 to Snake Head 
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #Check for head collisions with body segments 
    for segment in segments: 
        if segment.distance(head) < 20: 
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            #Hide the segments 
            for segments in segments: 
                segment.goto(2000, 2000)

            #Clear the segments list 
            segments.clear()    


    time.sleep(delay)

wn.mainloop()