import turtle
import random
t= turtle. Turtle()
t.width(10)
turtle.bgcolor("black")
color=["blue","yellow","red","pink","green"]


def drawit(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    star(100)

def star(length):
     length = random.randint(30,100)
     for i in range(5):
        t.fd(length)
        t.lt(144)
        t.color(random.choice(color))


#moon 달그리기 함수 
def moon():
      t.up()
      t.goto(-200,200)
      t.down()
      t.color("yellow")
      t.begin_fill()
      t.circle(70)
      t.end_fill()

s=turtle.Screen()
s.onscreenclick(drawit)
d=moon()

