                             ####################LECTURE 3###################
#####decisions
#conditionals
#if BOOLEAN EXPRESSION:   so the condition /boolean expression = (True/False, ==,!=, <, >, >=,<=, and, or, not)
#    DOsOMETHING()         execute this
#else:                    if it doesn't comply with the condition then
#    dosomethingelse()     execute this

#you can chain or nest
#if x<y:
#    print(x si less than y)
#else x>y:
#   print (x is bigger than y)
#   else:
#       print(x is equal to y)

####or
#if x<y:
#    print(x si less than y)
#elif x>y:
#   print (x is bigger than y)
#else:
#   print(x is equal to y)

##########while (general form of iteration... it depends on other conditions so the variables should change)
#the while fn... while something is true it keeps executing.
#while x>y:
#   print(x is bigger than y) this will result in an infinite loop(still evaluate one value of x)
#so x should change in time

#######acumulator pattern
#total = 0
#for x in range(10):
#   total = total + x
#or in while loop

total = 0     #define the count
x = 0         #define the variable
while x < 10:  #define the loop and its limits
   total = total + x   #add them 
   x = x + 1   #make x to change in time
print(total)   #45
print(x)       #10

total = 0     #define the count
x = 0         #define the variable
while total < 10:  #define the loop and its limits
   total = total + x   #add them 
   x = x + 1   #make x to change in time
print(total)   #10 look excel
print(x)       #5

##########blackjack
#Instructions:
#bank draws card
#check the player is busted or has 21
    #player gets another card
    #player gets choice to take another card
#if the player is busted:
    #lose
#if not:
    #check wether the bank is busted or 17 or higher
        #bank draws card
    #check

import random

def drawcard(total):
    card = random.randint(1,11)
    total = total + card
    print ("the card is a", str(card))
    print ("the total is now", str(total))
    return total

def blackjack():
    banktotal = 0
    playertotal = 0
    
#bank draws card
    banktotal = banktotal + drawcard(banktotal)
    playertotal = drawcard(playertotal)

#check the player is busted or has 21
    playerwantscard = True
    while playertotal<21 and playerwantscard:
        
    #if playertotal > 21:
    #    print "busted"
    #elif playertotal == 21:
    #    print "blackjack"
    #else
    #player gets another card
        card = input ("do you want another card? y/n")
        if card != "y":
            playerwantscard = False
        else:
            playertotal = drawcard(playertotal)

#if the player is busted:
    if playertotal>21:
        print("you are busted")
    else:
        while banktotal < 17:
            banktotal = drawcard(banktotal)
        if banktotal > 21:
           print("bank busted")
        elif playertotal > banktotal:
            print("you win")
        elif playertotal == banktotal:
            print("it's a draw")
        else:
            print ("bank win")
    #lose

blackjack()
