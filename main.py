import turtle
import time
import random

delay = 0.1
score =0
high_score = score
# setting up the window
wn = turtle.Screen()
wn.title("Scorpio")
wn.bgcolor("dark slate blue")
wn.setup(width=600, height=600)
wn.tracer(0)


# SNAKE HEAD
head = turtle.Turtle()
head.shape("square")
head.speed(0)
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# SNAKE FOOD
food = turtle.Turtle()
food.shape("circle")
food.color("light cyan")
food.penup()
x_pos = random.randint(-290,290)
y_pos = random.randint(-280,280)
food.goto(x_pos, y_pos)

# SCORINGS
pen = turtle.Turtle()
pen.shape("square")
pen.color("black")
pen.penup()
pen.goto(0, 260)
pen.hideturtle()


# SNAKE BODY
segments = []

# FUNCTIONS
def move():
    '''it helps the snake to move in different directions'''
    if head.direction == "up":
        y = head.ycor()
        # if y < 280:
        head.sety(y + 20)
        # else:
        #     new_segment.clear()
        #     head.goto(0, 0)
        #     segments.clear()
        #     head.direction = "stop"
            

    if head.direction == "down":
        y = head.ycor()
        # if y > -280:
        head.sety(y - 20)
        # else:
        #     head.goto(0, 0)
        #     head.direction = "stop"
        #     segments.clear()as it was always

    if head.direction == "right":
        x = head.xcor()
        # if x < 280:
        head.setx(x + 20)
        # else:
        #     head.goto(0, 0)
        #     head.direction = "stop"
        #     segments.clear()

    if head.direction == "left":
        x = head.xcor()
        # if x > -280:
        head.setx(x - 20)
        # else:
        #     segments.goto(1000,2000)
        #     head.goto(0, 0)
        #     head.direction = "stop"
        #     segments.clear()



# reffering the directions using 
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"
# --------------


# key bindings
wn.listen()
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')


# game loop
while(True):
    wn.update()
    
  
    y = head.ycor()
    x = head.xcor()
    if (y > 280 or y < -280 or x > 280 or x <-280):
        score = 0
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # this shit removes the segments after colliding
        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()

# c++ or at the things or just ta
    # snake colliding its own body
    for segment in segments:
        if segment.distance(head) < 20:
            score = 0
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()

    if head.distance(food) < 20:
        score += 1  
        # print(score)  
            
        # replace food at a random location
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.color("cyan")
        new_segment.penup()
        new_segment.shape("circle")
        segments.append(new_segment)

    # move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move the 0th index to head's position
    if len(segments) > 0: 
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    # HIGHSCORE
    
    if score > high_score:
        high_score = score

    pen.clear()
    pen.write(f"Score : {score}   High Score : {high_score} ", align = "center", font= ("Courier", 24, "normal"))


    move()
    time.sleep(delay)


wn.mainloop()
