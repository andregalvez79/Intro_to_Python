               ####################LECTURE 5###################

#\t is tab
#\r is return
#\n is new line
#\a appneds so it starts where it finished doesn't rewrite
#.format for strings is helpful

### handling files ###
# myfile = open ("file.txt", "r" to read) 
# if you use a for loop it read all the lines.
# myfile.close()
# myfile = open ("file.txt", "w" to write) 
#
# myfile.close()
#if file doesn't exist it'll create the file

###### iteration in files
#qbfile = open("qbdata.txt", "r")

#for aline in qbfile:
#    values = aline.split()
#    print('QB ', values[0], values[1], 'had a rating of ', values[10] )

#qbfile.close()

#### with while
#infile = open("qbdata.txt", "r")
#line = infile.readline()
#while line:
#    values = line.split()
#    print('QB ', values[0], values[1], 'had a rating of ', values[10] )
#    line = infile.readline()

#infile.close()

#### get a new file with data inside another file
#and create another file with this new data.

#infile = open("qbdata.txt", "r")      original file to read
#outfile = open("qbnames.txt", "w")    new created file to write what happens on the while

#aline = infile.readline()         set the while loop limit which is the number of lines
#while aline:       while there is a line
#    items = aline.split()            split the items
#    dataline = items[1] + ',' + items[0]       the second and first and add a comma in between
#    outfile.write(dataline + '\n')    once finished teh above add a new line         
#    aline = infile.readline()         do the same for the next line

#infile.close()
#outfile.close()

#### dictionaries have keys within a list
# and you can recall them like object[key] and look at what are the keys with
# .keys() and create a list
# iterate through dict with for (iteration through keys)
dictionary = {"thijs":33}
#to add more
dictionary["klaas"] = 34
print(dictionary)
for i in dictionary:
   print (i)

for key in dictionary.keys():
   print(key)

for value in dictionary.values():
   print(value)
#but no specific order, so you should make a list (not working)
print(dictionary.keys())
list1 = dictionary.keys()
print(list1)
#list1.sort()
for i in list1:
   print(list1)

#creates a list with duples
print(dictionary.items)
for key, value in dictionary.items():
   print(key,value)

#The del statement removes a key-value pair from a dictionary
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
del inventory['pears']
#assign new keys
inventory['pears'] = 0
#or
inventory ["bananas"] = inventory["bananas"] + 200

## to get info out of the dict
print(list(inventory.values()))
print(list(inventory.items()))

for (k,v) in inventory.items():
    print("Got", k, "that maps to", v)
#or the same as the for above
for k in inventory:
    print("Got", k, "that maps to", inventory[k])

#similar to lists with the in
print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")

#since “cherries” is not a key, return 0 (instead of None).
print(inventory.get("cherries", 0))

### matrixes
matrix = [[0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 2, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 3, 0]]
#or
matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}

#to access an element specifies the row 0 value 3
matrix[(0, 3)]
#to get acces to values zero use get 
print(matrix.get((0,3)))
print(matrix.get((1, 3), 0))
