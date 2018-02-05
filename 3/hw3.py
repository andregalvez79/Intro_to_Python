############ HW3 andre vargas

### DART/PI

import turtle
import math
import random

fred = turtle.Turtle()
fred.speed(10)

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)

def drawCircle(someturtle):
    someturtle.up()
    someturtle.goto(0, -1)
    someturtle.down()
    someturtle.circle(1, 360, 1000)
def drawSquare(someturtle):
    someturtle.up()
    someturtle.goto(1, -1)
    someturtle.down()
    for square in range(4):
        someturtle.lt(90)
        someturtle.fd(2)

drawCircle(fred)
drawSquare(fred)


numdarts = 10000
insidecount = 0.0
for i in range(numdarts):
    fred.penup()
    randx = random.uniform(-1.0,1.0)
    randy = random.uniform(-1.0,1.0)
    fred.goto(randx, randy)
    
    if fred.distance(0,0) <= 1:
       fred.color('red')
       fred.stamp()
    else:
       fred.color("blue")
       fred.stamp()
    if fred.distance(0,0) <= 1:
      insidecount = insidecount + 1
print(insidecount, "darts are inside the circle")

pi = (insidecount/numdarts)*4
print(float(pi))
    

#wn.exitonclick()

############################# BOOLEAN
#1
#Trure
#False
#False
#False


#2
#a <= b
#a < b  
#a<17 and day!=3
#a<17 or day==3

#3
def getgrades(mark):
  if mark >= 90:
    return "A"
  else:
    if mark >= 80:
      return "B"
    else:
      if mark >= 70:
        return "C"
      else:
        if mark >= 60:
          return "D"
        else:
          return "F"

mark = 79
print(getgrades(mark))
print(mark)

#4
#import turtle

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill() # stop filling this shape
    



xs = [48, 117, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 5

wn = turtle.Screen()             # Set up the window and its attributes
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.pensize(3)

def fillColor(t,height):
  if height >=200:
    t.fillcolor("red")
  elif height >= 100 and height < 200:
    t.fillcolor("yellow")
  else:
    t.fillcolor("green")
  drawBar(t,height)


for a in xs:
    fillColor(tess, a)

wn.exitonclick()

#5
#import turtle

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    if height < 0:
        t.write(str(height))
    t.left(90)
    t.forward(height)
    if height >= 0:
        t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape



xs = [48, -50, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)
minheight = min(xs)
numbars = len(xs)
border = 10

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)

wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")
if minheight > 0:
    lly = 0
else:
    lly = minheight - border

wn.setworldcoordinates(0-border, lly, 40*numbars+border, maxheight+border)


for a in xs:
    drawBar(tess, a)

#wn.exitonclick()



#6
from test import testEqual

def findHypot(a,b):
    asqr = a**2
    bsqr = b**2
    c = (asqr+bsqr)**.5
    return c

testEqual(findHypot(12.0, 5.0), 13.0)
testEqual(findHypot(14.0, 48.0), 50.0)
testEqual(findHypot(21.0, 72.0), 75.0)
testEqual(findHypot(1, 1.73205), 1.999999)

#7

#from test import testEqual

def is_even(n):
    if n%2 == 0:
      return True
    else:
      return False

testEqual(is_even(10), True)
testEqual(is_even(5), False)
testEqual(is_even(1), False)
testEqual(is_even(0), True)

#8
from test import testEqual

def is_even(n):
    if n%2 != 0:
      return True
    else:
      return False

testEqual(is_even(10), True)
testEqual(is_even(5), False)
testEqual(is_even(1), False)
testEqual(is_even(0), True)


#9
#from test import testEqual

def is_odd(n):
  if n%2 != 0:
    return True
  else:
    return False
def is_even(n):
  if is_odd(n):
    return True
  else:
    return False
testEqual(is_odd(10), False)
testEqual(is_odd(5), True)
testEqual(is_odd(1), True)
testEqual(is_odd(0), False)

#10
#from test import testEqual

def is_rightangled(a, b, c):
    if abs(c**2 - (a**2 + b**2)) < 0.001:  #si c**2 se aproxima a a**2 + b**2
      return True
    else:
      return False
    
    

testEqual(is_rightangled(1.5, 2.0, 2.5), True)
testEqual(is_rightangled(4.0, 8.0, 16.0), False)
testEqual(is_rightangled(4.1, 8.2, 9.1678787077), True)
testEqual(is_rightangled(4.1, 8.2, 9.16787), True)
testEqual(is_rightangled(4.1, 8.2, 9.168), False)
testEqual(is_rightangled(0.5, 0.4, 0.64031), True)

#11


