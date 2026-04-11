from turtle import*
import random
import time 
sc=Screen()
sc.bgcolor("light blue")
dart=Turtle()
dart.speed(0)
dart.shape("triangle")
dart.color("red")
dart.up()
dart.setheading(90)
dart.goto(0,-350)
pen=Turtle()
pen.hideturtle()
pen.speed(0)
pen.up()
pen.goto(0,350)
pen.write("Pop the balloon!",align="center",font=("arial",30,"bold"))
score=0
def show_score():
    pen.goto(-400,350)
    pen.write("score:{}".format(score),font=("arial",20,"bold"))
show_score()
def left():
    if dart.xcor()>-400:
        dart.setx(dart.xcor()-20)
def right():
    if dart.xcor()<400:
        dart.setx(dart.xcor()+20)
sc.listen()
sc.onkey(left,"Left")
sc.onkey(right,"Right")
balloons=[]
def create_balloons():
    global s
    b=Turtle()
    b.shape("circle")
    b.up()
    b.color(random.choice(["green","blue","purple","brown","orange"]))
    b.goto(random.randint(-350,350),400)
    s=(random.randint(1,3))
    bomb=random.random()
    if bomb<0.2:
        b.color("black")
    balloons.append(b)
before=time.time()
while True:
    sc.update()
    if time.time()-before>2:
        create_balloons()
        before=time.time()
    for b in balloons:
        b.sety(b.ycor()-10)
        if b.ycor()<-400:
            b.hideturtle()
            balloons.remove(b)
        elif dart.distance(b)<20:
            if b.color=="black":
                print("gameover")
                bye()
            else:
                score+=10
                show_score()
            b.hideturtle()
            balloons.remove(b)
done()