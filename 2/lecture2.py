##########
#lecture 2
#errors: semnatic, syntax, runtime
#modules and functions are building blocks...
#modules are already existing packages and functions you make yourself
#you can use modules with: import, from moduleimport function, dir() gives all functions

#example
import math
#gets the pi number
math.pi
#gest you all the functions in math
dir(math)
#you can searhc on python documentation and read what things do
#random gives you a random # (0,1), randrange gives you the same but within a specified range e.g. (1,19)
#shuffle() randomizes the order of a list

#turtlesinterface to move stuff around the screen
#donatello = turtle.Turtle() #so module = turtle . || Turtle is a class (which is template with features (legs, head, shell))

#example
import turtle
wn = turtle.Screen() #creates a window
donatello = turtle.Turtle() #creates a turtle in the window and defines the turtle module to donatello object
donatello.shape("turtle") #now the object that has been defined as a turtle can use the classes of turtle like shape
donatello.color("purple") #color
donatello.forward(100) #or forward which moves the object
wn.exitonclick()

#attributes can change... and have values. speed, slow or fast

#if you have several objects with a module instead of typing all you type:
#for "thing" in "listofthings":
#dosomethingwith(thing)
#list variables
x = ["item1", "item2", "item3"]
x = [1, 2, 3]
x = [1, "item2", 3.2]

#example
#import morning
#allteeth = [ molars, etc...]
#for tooth (this variable tooth is defined here) in allteeth:
#tooth.brush()

#range() returns list counting from 0 so instead of list [0,1,2,3] you can just range (4) it's the same.
#so it executes 4 times the method of the object who has been assigned to the module
#e.g. donatello.forward(100) four times
#you can define the range of range() with start(integer), stop(integer), and step(integer)

#module: yoga example
#classes of yoga: Yogi
#methods of Yogi class: downwarddog, plank, cobra, warrior2, triangle
#classes can have atributtes of Yogi: (tall, asian, etc...)
#x = yoga.Yogi()
#for positions in range (4):
    #x.plank()
    #x.cobra()
    #x.downwarddog
#for positions in range (2):
    #x.warrior2()
    #x.triangle()

################################################################################
#functions
#modules can also have functions or classes
#def es define a function
#eg:
#def drawSquare(turtle, size):
#   for i in range(4):
#       turtle.forward(size)
#       turtle.left(90)
#draws a square with a turtle , with a size of pixels.
#donatello = turtle.Turtle
#drawSquare(donatello, 50)

#local (within fn) vs global (outside a fn) scope.
#local is temporary
#global is persistent
#this hierarchy is given by indentation so a local is within a function.

#example
def forloop():  #a function
    j=i+1       #this is what the function does.
    return i    # this is the only way to retrieve local variables

i=10
forloop()
print(i) #when you print i is 10 beacuse i is a global variable defined forst even id its later... beacuse
print(j) #of indentention hierarchy, j doesn't exist outise de fn

#function that returns values (fruitful)
#functions can call other functions

def square(x):
    y = x*x
    return y
def sumsquares (x,y,z):
    a = square (x)
    b = square (y)
    c = square (z)
    return(a+b+c)

import turtle

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape



xs = [48, 117, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()             # Set up the window and its attributes
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)


for a in xs:
    drawBar(tess, a)

wn.exitonclick()

