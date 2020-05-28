import turtle
import os
import time

wn = turtle.Screen()
wn.title("Ping-Pong by Pratt")
wn.bgcolor("black")
wn.setup(width=800, height = 600)
wn.tracer(0)                    #doesnt updte window, faster exe

#variable initialization
score_a = 0
score_b = 0
ballSpeed_inc = 0.01
end_score = 10

#paddle 1
paddle_a = turtle.Turtle()
paddle_a.speed(0)               #set speed to max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=7, stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle 2
paddle_b = turtle.Turtle()
paddle_b.speed(0)               #set speed to max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=7, stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)                   #set speed to max
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1                   #ball x coor speed
ball.dy = 0.1                   #ball y coor speed

# paddle a movement
def paddle_a_up():              #moving 'a' up
    y = paddle_a.ycor()
    y += 20
    if y>230:
        y=230
    paddle_a.sety(y)
def paddle_a_down():            #moving 'a' down
    y = paddle_a.ycor()
    y -= 20
    if y<-230:
        y=-230
    paddle_a.sety(y)
wn.listen()                     #read keyboard ip
wn.onkeypress(paddle_a_up, "w")
wn.listen()                     #read keyboard ip
wn.onkeypress(paddle_a_down, "s")

# paddle b movement
def paddle_b_up():              # moving 'b' up
    y = paddle_b.ycor()
    y += 20
    if y>230:
        y=230
    paddle_b.sety(y)
def paddle_b_down():            # moving 'b' down
    y = paddle_b.ycor()
    y -= 20
    if y<-230:
        y=-230
    paddle_b.sety(y)
wn.listen()                     # read keyboard ip
wn.onkeypress(paddle_b_up, "Up")
wn.listen()                     # read keyboard ip
wn.onkeypress(paddle_b_down, "Down")

# pen
pen = turtle.Turtle()
pen.speed(0)                    # animation speed
pen.color("white")
pen.penup()                     #starts at origin we dont want to draw unwanted line
pen.hideturtle()                # only text is needed pen need not be shown
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align= "center",font=("Courier", 24, "normal") )

# main game loop
while True:
    wn.update()                     # update screen when someone wins

    # moving ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align= "center",font=("Courier", 24, "normal") )
        if ball.dx<0:
            ball.dx -= ballSpeed_inc
        else:
            ball.dx += ballSpeed_inc
        if ball.dy<0:
            ball.dy -= ballSpeed_inc
        else:
            ball.dy += ballSpeed_inc

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align= "center",font=("Courier", 24, "normal") )
        if ball.dx<0:
            ball.dx -= ballSpeed_inc
        else:
            ball.dx += ballSpeed_inc
        if ball.dy<0:
            ball.dy -= ballSpeed_inc
        else:
            ball.dy += ballSpeed_inc


    #Paddle collision with ball and rebound
    if (ball.xcor() > 340)and (ball.xcor()<350) and (ball.ycor() < paddle_b.ycor() + 60) and (ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if (ball.xcor() < -340)and (ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60) and (ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if score_a==end_score or score_b==end_score:
        pen.penup()                     #starts at origin we dont want to draw unwanted line
        pen.goto(0, 0)
        pen.write("GAME OVER", align = "center", font=("Courier", 48, "normal"))
        pen.penup()                     #starts at origin we dont want to draw unwanted line
        pen.goto(0, -40)
        if score_a > score_b:
            pen.write(" PLAYER A is the winner ", align = "center", font=("Courier", 24, "normal"))
        else:
            pen.write(" PLAYER B is the winner ", align = "center", font=("Courier", 24, "normal"))
        time.sleep(3)
        turtle.bye()


