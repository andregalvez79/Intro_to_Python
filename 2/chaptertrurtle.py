#turtles
import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()      # create a turtle named alex
alex.forward(150)           # tell alex to move forward by 150 units
alex.left(90)               # turn by 90 degrees
alex.forward(75)            # complete the second side of a rectangle
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(75)
#wn.exitonclick() #apparently this doesnt allow to close and open new screens
#so i comment it out

#changing properties or attributes


#wn = turtle.Screen()
wn.bgcolor("lightgreen")        # set the window background color

x = turtle.Turtle()
x.color("blue")              # make tess blue
x.pensize(3)                 # set the width of her pen

x.forward(50)
x.left(120)
x.forward(50)

#wn.exitonclick()                # wait for a user click on the canvas


#extension
#changing properties or attributes
#import turtle #it's not necessary to import it again

wn = turtle.Screen()
color_str = input("type the color of the background")
print(color_str)
wn.bgcolor(color_str)        # set the window background color

tess = turtle.Turtle()
colort_str = input("type the color of the turtle")

tess.color(colort_str)              # make tess a color
size_str = input("type the size of the pen")
tess.pensize(int(size_str))                 # set the width of her pen

tess.right(90)
tess.forward(80)
tess.left(190)
tess.forward(110)

wn.exitonclick()                # wait for a user click on the canvas

##############
#for loop
for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hi", name, "Please come to my party on Saturday!")
#executes the print for every name in the list once

#it can be used for commands too... it's gonna crash because of the wn problem
#import turtle            # set up alex
#wn = turtle.Screen()
#alex = turtle.Turtle()

#for i in [0, 1, 2, 3]:      # repeat four times
#    alex.forward(50)
#    alex.left(90)

#wn.exitonclick()
#### you can also sepcify this values as str or properties of a class
#import turtle            # set up alex
#wn = turtle.Screen()
#alex = turtle.Turtle()

#for aColor in ["yellow", "red", "purple", "blue"]:
#   alex.color(aColor)  #itll draw one line in yellow, then red, then purple then blue
#   alex.forward(50)
#   alex.left(90)

#wn.exitonclick()

########
#instead of a list in the for loop thi is legal too
#for i in range(4):   #this means [0,1,2,3]
    # Executes the body with i = 0, then 1, then 2, then 3
#for x in range(10): 
    # sets x to each of ... [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#this is legal too: range(1,5) this is [1,2,3,4]

print(range(4))
print(range(1, 5))

#or more complicated: range(start, stop, step)
print(range(0, 19, 2))
print(range(0, 20, 2))
print(range(10, 0, -1))

#cool stuff
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

print(range(5, 60, 2)) #range starts on 5 ends 59 and skips two
tess.up()                     # this is new
for size in range(5, 60, 2):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(size)          # move tess along
    tess.right(24)              # and turn her

wn.exitonclick()
#################################################################
#chapter functions
#import turtle

def drawSquare(t, sz): #here you define the structure of the function name(variables)
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz) #this is what will happen in the funtion
        t.left(90) #(this is a constant)


wn = turtle.Screen()              # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()            # create alex
drawSquare(alex, 50) #here you recall the function and t, is substituted for the object turtle and you define the size

wn.exitonclick()

#you can use functions in for loops example:
#def drawMulticolorSquare(t, sz):
#    """Make turtle t draw a multi-colour square of sz."""
#    for i in ['red','purple','hotpink','blue']:
#        t.color(i)
#        t.forward(sz)
#        t.left(90)
#wn = turtle.Screen()             # Set up the window and its attributes
#wn.bgcolor("lightgreen")

#tess = turtle.Turtle()           # create tess and set some attributes
#tess.pensize(3)

#size = 20                        # size of the smallest square

#for i in range(15):
#    drawMulticolorSquare(tess, size)      THIS IS THE FUNCTION
#    size = size + 10             # increase the size for next time
#    tess.forward(10)             # move tess along a little
#    tess.right(18)               # and give her some extra turn
#wn.exitonclick()

#in a function definition if you add return a varaible it will return a value...
#sounds obvious but if you don't then it just computes
#but can't see the result... ALSO RETURN ENDS THE FUNCTION... 
