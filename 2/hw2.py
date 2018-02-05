#HW2
#turtles
#1
for i in range (1000):
    print("We like Python's turtles!")

#2
for months in ["January", "February", "March", "April", "May", "June", "July", "August", "Septemeber", "October", "November", "December"]:
    print("One of the months of the year is",months)

#3
for num in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
    print(num)
    print(num**2)

#4 draw figures
import turtle
wn = turtle.Screen()
one = turtle.Turtle()
two = turtle.Turtle()
three = turtle.Turtle()
four = turtle.Turtle()

one.color("blue")
two.color("green")
three.color("red")
four.color("black")

for t in range(3):
    one.forward(20)
    one.left(360/3)
for i in range(4):
    two.forward(100)
    two.left(360/4)
for i in range(6):
    three.forward(30)
    three.left(360/6)
for i in range(8):
    four.forward(45)
    four.left(360/8)

#wn.exitonclick()

#6 asking someone
#import turtle
#wn = turtle.Screen()
one = turtle.Turtle()
two = turtle.Turtle()
three = turtle.Turtle()
four = turtle.Turtle()

colorone = input("what color do you want to use for the first figure?")
colortwo = input("what color do you want to use for the second figure?")
colorthree = input("what color do you want to use for the third figure?")
colorfour = input("what color do you want to use for the fourth figure?")

one.color(colorone, colorone) #use the same color for the fill next to coma
two.color(colortwo,colortwo)
three.color(colorthree,colorthree)
four.color(colorfour, colorfour)

sizeone = input("what size do you want to use for the first figure?")
sizetwo = input("what size do you want to use for the second figure?")
sizethree = input("what size do you want to use for the third figure?")
sizefour = input("what size do you want to use for the fourth figure?")

sideone = input("how many sides do you want to use for the first figure?")
sidetwo = input("how many sides do you want to use for the second figure?")
sidethree = input("how many sides do you want to use for the third figure?")
sidefour = input("how many sides do you want to use for the fourth figure?")

one.begin_fill() #to fill
for t in range(int(sideone)):
    one.forward(int(sizeone))
    one.left(360/int(sideone))
one.end_fill() #to end fill

two.begin_fill()
for i in range(int(sidetwo)):
    two.forward(int(sizetwo))
    two.left(360/int(sidetwo))
two.end_fill()

three.begin_fill()
for i in range(int(sidethree)):
    three.forward(int(sizethree))
    three.left(360/int(sidethree))
three.end_fill()

four.begin_fill()
for i in range(int(sidefour)):
    four.forward(int(sizefour))
    four.left(360/int(sidefour))
four.end_fill()

#wn.exitonclick()

#7
#import turtle
#wn = turtle.Screen()
pirate = turtle.Turtle()
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    pirate.left(angle)
    pirate.forward(100)

print("The pirate's final heading was", pirate.heading())

#wn.exitonclick()

#8 i would just say the guy was on drugs

#9 pentagraaaam!
#import turtle
#wn = turtle.Screen()
pent = turtle.Turtle()

for i in range(5):
    pent.forward(150)
    pent.left(36-180)

#wn.exitonclick()

#10 turtle clock
#import turtle
#wn = turtle.Screen()
wn.bgcolor("lightgreen")
clo = turtle.Turtle()
clo.shape("turtle")
clo.color("blue")

for i in range(12):
    clo.penup()
    clo.forward(100)
    clo.stamp()
    clo.pendown()
    clo.forward(-30)
    clo.penup()
    clo.forward(-70)
    clo.left(360/12)
#wn.exitonclick()

#11creative?
#import turtle
#wn = turtle.Screen()
clo = turtle.Turtle()
clo.speed(20)

for i in range(100):
    clo.color("blue")
    clo.forward(i)
    clo.left(13)
    clo.color("red")
    clo.forward(i)
    clo.right(50)
#wn.exitonclick()

#12 turtle type
#import turtle
clo = turtle.Turtle()
print(type(clo))
#<class '__main__.Turtle'>


#13
#import turtle
#wn = turtle.Screen()
sprite = turtle.Turtle()
nlegs = int(input("How many legs should this sprite have? "))
total = 360 / nlegs

for i in range(nlegs):
    sprite.forward(100)
    sprite.stamp()
    sprite.backward(100)
    sprite.right(total)
sprite.shape("circle")

#wn.exitonclick()

################################################################################
#modules
#1 print 10 random numbers
import random
for i in range(10):
    rand = random.random()
    print(rand)


#2print 10 randnums within a range of 25 and 35
#import random
for i in range(10):
    rand = random.randint(25,36)
    print(rand)

#3 pythagoras
import math
a = 5
b = 10
c = math.hypot(a,b)
print(c)

#Gregory-Leibniz series to calculate Pi.... copied wtf?
#import math
def make_pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(1000):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2

digits = make_pi()
pi_list = []
my_array = []

for i in make_pi():
    my_array.append(str(i))

my_array = my_array[:1] + ['.'] + my_array[1:]
big_string = "".join(my_array)
print "here is a big string:\n %s" % big_string 

import math
print ("here is the math.pi value:" math.pi)

#############################################################
#functions

#1

#import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)
      

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("red")

for i in range (5):
    drawSquare(alex, 20)
    alex.penup()
    alex.forward(40)
    alex.pendown()

#wn.exitonclick()

#2
#import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)
      

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("red")

for i in range (5):
    n = 20*i 
    drawSquare(alex, n)
    alex.penup()
    alex.forward(-10)
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()
    

#wn.exitonclick()

#3
#import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("red")

def drawPoly (t,s,l):
    for i in range (s):
        t.pendown()
        t.forward(l)
        t.left(360/s)

drawPoly(tess, 8, 50)

#wn.exitonclick()

#4
#import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)
      

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("blue")
alex.speed(100)

for i in range (18):
    drawSquare(alex, 100)
    alex.left(20)

#wn.exitonclick()

#5
#first part

#import turtle
def drawspiral(t,angle):
    size = 1
    for i in range (100):
        t.forward(size)
        t.left(angle)
        size = size + 3
        
wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("blue")
alex.speed(100)

drawspiral(alex,90)

#second part

alex.penup()
alex.home()
alex.color("red")
alex.pendown()

drawspiral(alex,89)

#wn.exitonclick()

#6
#import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("red")

def drawPoly (t,s,l):
    for i in range (s):
        t.pendown()
        t.forward(l)
        t.left(360/s)

def drawEquitriangle(t,sz):
  drawPoly(t,3,sz)

drawEquitriangle(tess,30)
wn.exitonclick()

#7 sumatoria
from test import testEqual

def sumTo(n):
    # your code here
    result =  (n * (n + 1)) / 2
    return result

result = sumTo(2)
print(result)
result2 =sumTo(5)
print(result2)

#8 area of circle
from test import testEqual
import math
def areaOfCircle(r):
    # your code here
    area = math.pi*r
    return area

t = areaOfCircle(0)
testEqual(t,0)
t = areaOfCircle(1)
testEqual(t,math.pi)
t = areaOfCircle(10000)
testEqual(t,31415.926535897932)

#9 star

#import turtle

def drawStar(t):
    for i in range(5):
        t.forward(100)
        t.left(216)

x = turtle.Turtle()
drawStar(x)

#10 extended star
#import turtle

def drawStar(t):
    for i in range(5):
        t.forward(50)
        t.left(216)
        
def multiple(t):
  for i in range(5):
    drawStar(t)
    #t.penup()
    t.forward(150)
    #t.pendown()
    t.right(144)
    

x = turtle.Turtle()
x.speed(100)
multiple(x)

#11
#import turtle
wn = turtle.Screen()
def drawStar(t,n):
    for i in range(n):
        t.forward(100)
        t.left(180 - 180/n)
    

x = turtle.Turtle()
x.speed(100)
drawStar(x,13)
#wn.exitonclick()

#12
#import turtle
wn = turtle.Screen()
sprite = turtle.Turtle()

def drawsprite(sp,lg,lh):
  total = 360 / lg
  for i in range(lg):
    sp.forward(lh)
    sp.stamp()
    sp.backward(lh)
    sp.right(total)
sprite.shape("circle")

drawsprite (sprite,15,120)
#wn.exitonclick()

#13
def sumTo(n):
  sum = 0
  for i in range(1,n+1):
      sum = sum + i
  return sum

t = sumTo(0)
print("The sum from 1 to 0 is",t)
t = sumTo(10)
print("The sum from 1 to 10 is",t)
t = sumTo(5)
print("The sum from 1 to 5 is",t)

#14 Newton square aprox

def mySqrt(n):
  iguess = n/2
  closer = (iguess + n/iguess)/2
  while closer != iguess:
    iguess = closer
    closer = (iguess + n/iguess)/2
  return iguess
  

x=100
closer = mySqrt(x)
print(closer)
print(x**.5)

#15.. no idea

#16

#import turtle

def drawSprite(t, numlegs, leglength):
   angle = 360/numlegs
   for i in range(numlegs):
      t.forward(leglength)
      t.backward(leglength)
      t.left(angle)

def drawFancySquare(t, sz, lgs, lgl):
   for i in range(4):
       t.forward(sz)
       drawSprite(t, lgs, lgl)
       t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
drawFancySquare(alex, 100, 10, 15)

wn.exitonclick()
