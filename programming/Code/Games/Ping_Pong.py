import turtle as tr
import random

x = 800
y = 600
window = tr.Screen()
window.title("Ping Pong")
window.setup(x, y)
window.tracer(0)
window.bgcolor("black")

b1 = tr.Turtle()
b1.shape("square")
b1.color("blue")
b1.penup()
b1.goto(-350, 0)
b1.shapesize(5, 1)
b1.speed(0)


b2 = tr.Turtle()
b2.shape("square")
b2.color("red")
b2.penup()
b2.goto(350, 0)
b2.shapesize(5, 1)
b2.speed(0)


ball = tr.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.shapesize(1, 1)
ball.speed(0)
ball.dx = random.choice([-1,1])
ball.dy = random.uniform(-0.7, 0.7)

CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')


button = tr.Turtle()
button.hideturtle()

writ = tr.Turtle()
writ.hideturtle()

nh = tr.Turtle()
nh.hideturtle()

p1 = 0
p2 = 0
score = tr.Turtle()
score.hideturtle()
score.penup()
score.color("white")
score.goto(0,260)
score.write(f"Player_1: {p1} player_2: {p2}",align="center", font="courier 14")
isesk = False
def up1():
    if b1.ycor() < 240:
        y = b1.ycor()
        y += 50
        b1.sety(y)

def down1():
    if b1.ycor() > -240:
        y = b1.ycor()
        y -= 50
        b1.sety(y)

def up2():
    if b2.ycor() < 240:
        y = b2.ycor()
        y += 50
        b2.sety(y)

def down2():
    if b2.ycor() > -240:
        y = b2.ycor()
        y -= 50
        b2.sety(y)

def esk():
    button.showturtle()
    button.shape('square')
    button.shapesize(3,3)
    button.fillcolor('grey')
    button.penup()
    button.goto(0, 0)
    writ.clear()
    writ.goto(0, -50)
    writ.color("white")
    writ.write("Restart", align='center', font=FONT)
    global nh
    nh.hideturtle()
    nh.shape("square")
    nh.color("white")
    nh.penup()
    nh.goto(0, 0)
    nh.shapesize(10, 10)
    nh.speed(0)
    global ball
    ball.goto(0, 0)  
    ball.hideturtle()
    global isesk
    isesk = True
    def restart(x, y):
        global ball
        ball.dx = random.choice([-1,1])
        ball.dy = random.uniform(-0.7, 0.7) 
        ball.goto(0, 0)  
        ball.showturtle()
        global nh
        nh.hideturtle()
        global isesk
        isesk = False
        score.clear()
        writ.clear()
        global p1
        p1 = 0
        global p2
        p2 = 0
        score.write(f"Player_1: {p1} player_2: {p2}",align="center", font="courier 14")
        button.hideturtle()
    window.listen()
    button.onclick(restart)


while True:
    window.update()
    window.setup(800,600)

    window.listen()
    window.onkeypress(up1, "w")
    window.onkeypress(down1, "s")
    window.onkeypress(up2, "Up")
    window.onkeypress(down2, "Down")
    window.onkeypress(esk , "Escape")

    ball.setx(ball.xcor() + ball.dx)

    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy = random.uniform(-0.7, 0.7)
        score.clear() 
        if isesk == False:
            p1 += 1
            score.write(f"Player_1: {p1} player_2: {p2}",align="center", font="courier 14")
        else:
            score.write(f"Player_1: {p1} player_2: {p2}",align="center", font="courier 14")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy = random.uniform(-0.7, 0.7)
        score.clear()
        if isesk == False:
            p2 += 1
            score.write(f"Player_1: {p1} player_2: {p2}",align="center", font="courier 14")
        else:
            score.write(f"Player_1: {p1} player_2: {p2}",align="center", font="courier 14")


    if 338 < ball.xcor() < 350 and ball.ycor() - b2.ycor() < 52 and ball.ycor() - b2.ycor() > -52:
        ball.dx *= -1

    if -338 > ball.xcor() > -350 and ball.ycor() - b1.ycor() < 52 and ball.ycor() - b1.ycor() > -52:
        ball.dx *= -1

