               ####################HW 4###################
#ANDRE VARGAS
####  STRINGS
##2
prefixes = "JKLMNOPQ"
suffix = "ack"
for p in prefixes:
  if p == "O" or p == "Q":
    print(p + "u" + suffix)
  else:
    print(p + suffix)


#3
def count(p):
    lows = "abcdefghijklmnopqrstuvwxyz"
    ups =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    numberOfe = 0
    totalChars = 0
    for achar in p:
        if achar in lows or achar in ups:
            totalChars = totalChars + 1
            if achar == 'e':
                numberOfe = numberOfe + 1

    percent_with_e = (numberOfe / totalChars) * 100
    print("Your text contains", totalChars, "alphabetic characters of which", numberOfe, "(", percent_with_e, "%)", "are 'e'.")


p = '''
"If the automobile had followed the same development cycle as the computer, a
Rolls-Royce would today cost $100, get a million miles per gallon, and explode
once a year, killing everyone inside."
-Robert Cringely
'''

count(p)

##6
from test import testEqual

def reverse(astring):
  if len(astring) <= 1:
    return astring
  return reverse(astring[1:]) + astring[0]

testEqual(reverse("happy"), "yppah")
testEqual(reverse("Python"), "nohtyP")
testEqual(reverse(""), "")

#7
from test import testEqual

def reverse(astring):
  if len(astring) <= 1:
    return astring
  return reverse(astring[1:]) + astring[0]

def mirror(astring):
  return astring + reverse(astring)

testEqual(mirror('good'), 'gooddoog')
testEqual(mirror('Python'), 'PythonnohtyP')
testEqual(mirror(''), '')
testEqual(mirror('a'), 'aa')

##8

from test import testEqual

def remove_letter(theLetter, theString):
   newstring = ""
   for ch in theString:
      if ch == theLetter:
         ch = ""
      newstring = newstring + ch
   return newstring
  
testEqual(remove_letter('a', 'apple'), 'pple')
testEqual(remove_letter('a', 'banana'), 'bnn')
testEqual(remove_letter('z', 'banana'), 'banana')

##10
from test import testEqual

def count(substr,theStr):
  cnt = 0
  idx = 0
  while True:
    idx = theStr.find(substr, idx)
    if idx >= 0:
      cnt += 1
      idx += 1
    else:
      break
  return(cnt)

testEqual(count('is', 'Mississippi'), 2)
testEqual(count('an', 'banana'), 2)
testEqual(count('ana', 'banana'), 2)
testEqual(count('nana', 'banana'), 1)
testEqual(count('nanan', 'banana'), 0)
testEqual(count('aaa', 'aaaaaa'), 4)

####LISTS

#3
a = [76,92.3, "hello", True, 4, 76]
print(a)

a.append(79)
a.insert(3,"cat")
a.insert(0,99)
print(a.index("hello"))
print(a.count(76))
a.pop(1)
if True in a:
  a.pop(4)
print (a)

##4
import random
b=[]
for i in range(100):
  b.append(random.randint(0,1000))
print(len(b))
print(b)

def avg (interval):
  x = sum(interval) / float(len(interval))
  return(x)

print(avg(b))

#5
import random
b=[]
for i in range(100):
  b.append(random.randint(0,1000))
print(len(b))
print(b)

def maxnum (interval):
  interval.sort()
  return interval[-1]

print(maxnum(b))

##6
x=[2,3,4]
def sumsq (l):
  return [i ** 2 for i in l]

print(sumsq(x))

##14
#########

###########
def replace (w,old,new):
  w.replace(old, new)
  return w


s = "I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!"
print(replace(s, "om", "am"))
print(replace(s, "o", "a"))
print(s.replace("o","a"))
