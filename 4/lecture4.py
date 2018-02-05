               ####################LECTURE 4###################
#STRINGS PT.2
#SPACES ALSO COUNT AS CHARACTERS
#two operations: + is concatenate and repetition is * (3*"string" = stringstringstring)
#indexing from left to right it's 0 to n number of characters and from right to left is from -1 to n
#slicing string would be like: string = "string" ... string[2:5] or [:3] not including three or [3:] start at 3 to the end
#object.strip() deletes spaces
#object.replace("x","y") replaces x to y, but you need to stroe it in a new var
#object.find(x) returns index (number of character) in a string where the x was found in the object (word or str)
#object.upper() upper case
#object.lower() lower case
#all str have a value in python you can tell with ord("a")
#uses ANSI code, to see use chr(1)
#only one uppercase
somestring = "monty python"
i=somestring.find("m")
somestring = somestring[:i] + somestring[i].upper() + somestring[i+1:]
print (somestring)
#or
newstring = ""
for ch in somestring:
   if ch == "p":
      ch = ch.upper() #because strings are inmutable you need to assign it to a variable
      newstring += ch  #update is +=
   else:
      newstring += ch

print(newstring)

#LISTS
#you dont need to assing lists to new vars it changes them... they are mutable.
mylist = [1,6]
mylist.append(7)
print(mylist)

mylist= [1,3,6] #count starts at 0 so it changes the 5
mylist[2] = "hong kong"
print(mylist)

mylist.append(5)
mylist[:3] #doesn't return the 5
print(mylist)

mylist.insert(2, "python")
print(mylist)


#mylist.sort() #doesnt work with strings in pyth 3.x
print(mylist) #orders the list so...

for i in range(len(mylist)):
	if type(mylist[i]) == int:
		mylist[i] = chr(mylist[i])

mylist.sort()
for i in range(len(mylist)):
	if len(mylist[i]) == 1:
		mylist[i] = ord(mylist[i])

print(mylist)

mylist.append ([1,2,3])
print(mylist) #the list is just another object in the list

list2 = mylist[-1][1]
print(list2) #will retunr the 2 from the list in the list

val = mylist.pop()
val #removes the last variable from the list
print(mylist)

#index... get the index and count... counts the vars in the list

#lists can share the same references or variables
#the only way to to do get one constant and the other changing is with a clone b = a[:]

#tuples not mutable
x,y,z =(4,5,6)
print (x)
print (y)
print (z)
#Besides the shallow difference that lists are created using brackets
#"[ ... , ... ]" and tuples using parentheses "( ... , ... )",
#the core technical "hard coded in Python syntax" difference between
#them is that the elements of a particular tuple are immutable whereas
#lists are mutable

#example list comprehension
mylist = [1,2,3,4,5]

yourlist = [item ** 2 for item in mylist if item %2 == 0]

print(yourlist)

print(mylist[3:1])
print(mylist[:2])
print(mylist[3:])
print(mylist[2:4])
