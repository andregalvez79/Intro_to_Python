     
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()

actions = [(100,90), (50,90), (100,45), (100,45), (50,90),(50,90)]
for action in actions:
   tess.forward(action[0])
   tess.left(action[1])
wn.exitonclick()

l= range(1,10)

print(l)
print (len(l))
print (range (0, len(l),3))

#for i in range (0, len(l),3):
#   l[i] = l[i-2]

print (l)

numbers = [5,7,2,3,4,5,3,5,2,7,7,5,9]
result=[]
print(len(numbers)-2)
for i in range (len(numbers)-2):
   n1 = numbers[i]
   print (n1)
   n2 = numbers [i+1]
   print (numbers [i+1])
   n3= numbers[i+2]
   print (numbers[i+2])
   if not (n1>n2 or n1<n3):
      result.append(n1)
      print(n1>n2)
      print(n1<n3)
print (result)

nums = [5,7,2,8,4,5,3,5,2,7,7,5,9]
res=[]

while len(res)<4:
   print(len(res))
   print([nums[len(res)]])
   print(nums[nums[len(res)]])
   res.append(nums[nums[len(res)]])
print (res)

t=0
for x in range(8):
   if x%3>0:
      t=t+x
print (t)

d = range(1,10)
print(range(1,10))

walrus ="I am here as you are here as we are all together"
new= ""
for i in range(len(walrus)):
   if walrus[i] == "a":
      new = new + walrus[i:i+3:2]
print (new)
