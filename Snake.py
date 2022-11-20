import turtle
import time
import random

delay = 0.2

#Set up the Screen

wn=turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#Snake head
head = turtle.Turtle()
head.speed(0) 
head.shape("triangle")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"


segments = []

#FOOd
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,200)

#Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"
    
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

#KEyboards Bindings
wn.listen()
wn.onkey(go_up, "w")
wn.onkey(go_left, "a")
wn.onkey(go_right, "d")
wn.onkey(go_down, "s")

#main game loop
while True:
    wn.update()

    #Collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #HIde Segments
        for segment in segments:
            segment.goto(10000,10000)

        #clear segment list
            segments = []

    if head.distance(food) < 20:
        #Move food
        x = random.randint(-290,+290)
        y = random.randint(-290,+290)
        food.goto(x,y)


        #Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    #MOVIng Body
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #Segment 0
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()



    time.sleep(delay)

wn.mainloop()
