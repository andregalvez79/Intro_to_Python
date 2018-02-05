               ####################HW 5###################
##Andre Vargas

#### FILES ####
#1 returns only the person with more tha 6 grades
testd = open("studentdata.txt", "r")

for aline in testd:
  values = aline.split()
  if len(values[1:]) > 6:
    print(values[0])

testd.close()

##2 retunrs the avg of grades with the name of the person
testd = open("studentdata.txt", "r")

for aline in testd:
  values = aline.split()
  grades = values[1:]
  grades = [int(i) for i in grades]
  avg = sum(grades)/len(values[1:])
  print(values[0],avg)

testd.close()

#5
import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-300, -300, 300, 350)

coord = open("mystery.txt", "r")

for aline in coord:
    values = aline.split()
    if values[0] == "DOWN":
        t.down()
    elif values[0] == "UP":
            t.up()
    else:
      t.goto(int(values[0]), int(values[1]))

coord.close()
wn.exitonclick()

#### Dictionaries ####
#1

sntc = input("Enter a sentence")

sntc = sntc.lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def countall (string):
  countdict = {}
  for ch in string:
    if ch in alphabet:
      countdict[ch] = string.count(ch)
  keys = countdict.keys()
  keys.sort()
  for ch in keys:
    print(ch, countdict[ch])

countall(sntc)

##2
##couning letters
#Define the function to require one parameter, the string.
#Create an empty dictionary of counts.
#Iterate through the characters of the string, one character at a time.

def countall (string):
   countdict = {}
   for ch in string:
      countdict[ch] = string.count(ch)
   return countdict

print(countall("banana"))

#5
#english to pirate
pirate = {}
pirate['sir'] = 'matey'
pirate['hotel'] = 'fleabag inn'
pirate['student'] = 'swabbie'
pirate['boy'] = 'matey'
pirate['restaurant'] = 'galley'
# and so on

sentence = input("Please enter a sentence in English")

psentence = []
words = sentence.split()
for aword in words:
    if aword in pirate:
        psentence.append(pirate[aword])
    else:
        psentence.append(aword)

print(" ".join(psentence))
