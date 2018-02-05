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

