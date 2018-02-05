Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 4+4
8
>>> 4.0+4.0
8.0
>>> "4"+"4"
'44'
>>> print("hello world")
hello world
>>> 
print(1+1)
2
>>> print(len("hello"))
5
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> x=1
>>> print(x)
1
>>> 8/3
2.6666666666666665
>>> 8.0/3
2.6666666666666665
>>> x=8
>>> y=3
>>> x/y
2.6666666666666665
>>> #in 2.7 you have to convert this to integer
>>> x/float(y)
2.6666666666666665
>>> input("question")
question
''
>>> age = raw_input ("what is your age?)
		 
SyntaxError: EOL while scanning string literal
>>> age = raw_input ("what is your age?")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    age = raw_input ("what is your age?")
NameError: name 'raw_input' is not defined
>>> 
