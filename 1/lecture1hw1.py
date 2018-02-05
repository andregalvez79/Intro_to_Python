4+4
4.0+4.0
"4"+"4"
print("hello world")
print(1+1)
x=1
print(x)
8/3
8.0/3
x=8
y=3
x/y
#in 2.7 you have to convert this to integer
x/float(y)
input("question")	 
age = input ("what is your age?")
print(age)
###################################################################################
#HW1
message = """This message will
span several
lines."""
print(message)

print("""This message will span
several lines
of the text.""")
#to use quotes within
print('''"Oh no", she exclaimed, "Ben's bike is broken!"''')
#to know which type is 17
print(type(17))
#first ok, second will separte two values 42 0.
print(42000)
print(42,000)

#The int function can take a floating point number or a string, and turn it into an int.
print(3.14, int(3.14))
print(3.9999, int(3.9999))       # This doesn't round to the closest int!
print(3.0, int(3.0))
print(-3.999, int(-3.999))        # Note that the result is closer to zero
print("2345", int("2345"))        # parse a string to produce an int

#float to change from str, int to float
print(float("123.45"))
print(type(float("123.45")))

#str turns its argument into a string
print(str(17))
print(str(123.45))
print(type(str(123.45)))

#reassignment of variables
day = "Thursday"
print(day)
day = "Friday"
print(day)
day = 21
print(day)

a = 5
b = a    # after executing this line, a and b are now equal
print(a, b)
a = 3    # after executing this line, a and b are no longer equal
print(a, b)
#no hace el update la formula a=b solo funciona para el primer step
#length of the variable (counts)-- result is 5
print(len("hello"))

#integer division is // which means that it will round up to 0
print(7 / 4)
print(7 // 4)

#x % y is zero, then x is divisible by y or  remainder after division.
print(7%3)
print(9%3)
print(3%9)

#input
n = input("Please enter your name: ") #propmts you with the question or instruction
#you answer
print("Hello", n) #prints hello answer

#NOTE: It is very important to note that the input function returns a string value.
#Even if you asked the user to enter their age, you would get back a string like "17".
#It would be your job, as the programmer, to convert that string into an int or a float,
#using the int or float converter functions we saw earlier.

str_seconds = input("Please enter the number of seconds you wish to convert")
total_secs = int(str_seconds)
hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60
print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)

#order is very mathematical (but always specify with parentesis)...
#when the same hierarchy in math the its from left to right except this case

print(2 ** 3 ** 2)     # the right-most ** operator gets done first! 2**9
print((2 ** 3) ** 2)   # use parentheses to force the order you want! 8**2

print(16 - 2 * 5 // 3 + 1)
#the expression is evaluated as (2*5) first, then (10 // 3), then (16-3), and then (13+1).

#update
x = 6        # initialize x
print(x)
x = x + 1    # update x
print(x)
#This means get the current value of x, add one, and then update x with the new value. 

#questions
#question 1
print(5 ** 2) #25
print(9 * 5) #45
print(15 / 12) #1.something
print(12 / 15) #.8 or something
print(15 // 12) #1
print(12 // 15) #0
print(5 % 2) #?
print(9 % 5) #4
print(15 % 12) #3
print(12 % 15) #?
print(6 % 6) #0
print(0 % 7) #0

#question 2
message1 = """first the parentesis
then multiplications and divisions
finally add."""
#2 + 2* 10/5 * 5
#2 + 100/5
# 2+20 = 22
print (message1)
print(2 + (3 - 1) * 10 / 5 * (2 + 3))

#question 3 alarm clock in 24 hrs
#set input
alarm_str = input("Please enter the amount of hours to set the alarm off")
time_str = input("Please enter what time is it (24hrs without :00)")
#change fromat
alarm_int = int(alarm_str)
time_int = int(time_str)
#add hours for total
hours = alarm_int + time_int
#put them in a limit of 24 hrs
hourscomplete = (hours % 24)
print(hours % 24)
#result which time will it be when the alarm sets off
#print never uses a "=" ... noob
print(hourscomplete)

#question 4
start_str = input("Please enter the number of the day in which you will start")
lenght_str = input("What is the lenght of your stay?(nights)")
#change fromat
start_int = int(start_str)
lenght_int = int(lenght_str)
#add days for total
days = start_int + lenght_int
#put them in a limit of 7 days
total = (days % 7)
print(total)

#question 5
#All work and no play makes Jack a dull boy
first = "All"
second = "work"
third = "and"
fourth = "no"
fifth = "play"
sixth = "makes"
seventh = "Jack"
eigth = "a"
ninth = "dull"
tenth = "boy."
print(first, second, third, fourth, fifth, sixth, seventh, eigth, ninth, tenth)

#question 6

print(6 * 1 - 2) #4
print(6 * (1 - 2)) #-6

#question 7
#compound interest calculator

P=10000
n=12
r=.08
time_str = input("how many years you wish to invest your 10,000?")
#change fromat
time_int = int(time_str)
total = (P*(1+(r/n))**time_int)
print(total)

#question 8 area of a circel calc
#A = pi*(r**2)
pi=3.1416
radius_str = input("What is the raidus of the circle?")
#change fromat
radius_int = int(radius_str)
A = pi*(radius_int**2)
#with friendly message
print ("The area of the circle with", radius_int, "of radius is:", A)

#question 9 area of rectangle
#A=w*l
w_str = input("What is the width of the rectangle?")
l_str = input("What is the lenght of the rectangle?")
#change fromat
w_int = int(w_str)
l_int = int(l_str)
A = w_int*l_int
#with friendly message
print ("The area of the rectangle with", w_int, "of width, and", l_int, "of lenght is:", A)

#question 10
#mpg = M/G
m_str = input("how many miles have you driven?")
g_str = input("how many galons have you used?")
#change fromat
m_f = float(m_str)
g_f = float(g_str)
mpg = m_f/g_f
print ("The MPG of your car is:", mpg)

#question 11
#celsius to farenheit... why?!!
C_str = input("what is the degrees in Celsius?")
#change fromat
C_f = float(C_str)
F = C_f * (9/5) + 32
print(C_f, " degrees Celsius is", F, " degrees Farenheit.")

#question 12
#farenheit to celsius... ok :)
F_str = input("what is the degrees in Farenheit?")
#change fromat
F_f = float(F_str)
C = (F_f - 32) * 5/9
print(F_f, " degrees Farenheit is", C, " degrees Celsius.")
