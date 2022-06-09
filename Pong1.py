# Simple Pong in Python 3 for Beginners
# By Nate B.
# Part 1: Getting started

import turtle

win = turtle.Screen()
win.title("Pong by Nate B.")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Function
def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)
	

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)
	
def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)
	

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)
	
# Keyboard binding
wn = turtle.listen()
wn = turtle.onkeypress(paddle_a_up, "w")
wn = turtle.onkeypress(paddle_a_down, "s")
wn = turtle.onkeypress(paddle_b_up, "Up")
wn = turtle.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
	 win.update()
	 
	 # Move the ball
	 ball.setx(ball.xcor() + ball.dx)
	 ball.sety(ball.ycor() + ball.dy)
	 
	 # Border checking
	 if ball.ycor() > 290:
		 ball.sety(290)
		 ball.dy *= -1
		 
	 if ball.ycor() < -290:
		 ball.sety(-290)
		 ball.dy *= -1
		 
		 
	 if ball.xcor() > 390:
		 ball.goto(0, 0)
		 ball.dx *= -1
		 
	 if ball.xcor() < -390:
		 ball.goto(0, 0)
		 ball.dx *= -1
		 
		 

		 
		 
     
		 
		 
	
