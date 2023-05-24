import turtle
w=turtle.Screen()
w.title('ping pong')
w.bgcolor('black')
w.setup(width=800,height=600)
w.tracer(0)


#Shape1


Shape1=turtle.Turtle()
Shape1.speed(0)
Shape1.penup()
Shape1.shape('square')
Shape1.color('red')
Shape1.goto(-360,0)
Shape1.shapesize(stretch_wid=6,stretch_len=1)


#Shape2



Shape2=turtle.Turtle()
Shape2.speed(0)
Shape2.penup()
Shape2.shape('square')
Shape2.color('blue')
Shape2.goto(360,0)
Shape2.shapesize(stretch_wid=6,stretch_len=1)
#if Shape2.ycor()>290 :
	#Shape2.goto(360,290)

#functions
def Shape1_Up():
	Shape1.sety(Shape1.ycor() + 30)
def Shape1_Down():
	Shape1.sety(Shape1.ycor() - 30)
def Shape2_Up():
	Shape2.sety(Shape2.ycor() + 30)
def Shape2_Down():
	Shape2.sety(Shape2.ycor() - 30)
w.listen()
w.onkeypress(Shape1_Up,'z')
w.onkeypress(Shape1_Down,'s')
w.onkeypress(Shape2_Up,'Up')
w.onkeypress(Shape2_Down,'Down')



p1=turtle.Turtle()
p1.shape('square')
p1.color('orange')
p1.penup()
p1.goto(0,300)
p1.shapesize(stretch_wid=1,stretch_len=40)
p1=turtle.Turtle()
p1.shape('square')
p1.color('orange')
p1.penup()
p1.goto(0,-300)
p1.shapesize(stretch_wid=1,stretch_len=40)
p2=turtle.Turtle()
p2.shape('square')
p2.color('orange')
p2.penup()
p2.goto(-390,0)
p2.shapesize(stretch_wid=29,stretch_len=1)
p2=turtle.Turtle()
p2.shape('square')
p2.color('orange')
p2.penup()
p2.goto(+390,0)
p2.shapesize(stretch_wid=29,stretch_len=1)

#ball

ball=turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.goto(0,0)
ball.penup()
ball.dx=1
ball.dy=1


#score
score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.hideturtle()
score.penup()
score.color('white')
score.goto(0,260)
score.write('Player1  :  0  ,  Player2  :  0  ',align='center',font=('courier',12,'normal'))




while True :
	w.update()
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)
	if ball.ycor()>290 :
		ball.sety(290)
		ball.dy *= -1
	if ball.ycor()<-290 :
		ball.sety(-290)
		ball.dy *= -1	
	if ball.xcor()>390 :						#here
		ball.goto(0,0)
		ball.dx *= -1
		score2 +=1
		score.clear()
		score.write('Player1  :   {}   ,  Player2 :   {}  '.format(score2,score1),align='center',font=('courier',12,'normal'))
	if ball.xcor()<-390 :
		ball.goto(0,0)
		ball.dx *= -1
		score1 += 1
		score.clear()
		score.write('Player1  :   {}   ,  Player2  :   {}  '.format(score1,score2),align='center',font=('courier',12,'normal'))
	if Shape2.ycor()>260 :
		Shape2.goto(360,240)
	if Shape2.ycor()<-260 :
		Shape2.goto(360,-240)
	if Shape1.ycor()>260 :
		Shape1.goto(-360,240)
	if Shape1.ycor()<-260 :
		Shape1.goto(-360,-240)
	if ball.xcor()>350 and ball.xcor()<360 and ball.ycor()<Shape2.ycor()+60 and ball.ycor()>Shape2.ycor()-60 :
		ball.setx(350)
		ball.dx *= -1
	if (ball.xcor()<-350 and ball.xcor()>-360 and ball.ycor()<Shape1.ycor()+60 and ball.ycor()>Shape1.ycor()-60) :
		ball.setx(-350)
		ball.dx *= -1
			

					
