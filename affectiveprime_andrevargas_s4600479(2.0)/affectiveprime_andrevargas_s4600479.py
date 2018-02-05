##########Affective priming task###############
#The task displays a prime (word or picture) followed by a target (positive or negative word) 
#it read the stimuli (names) from an excel file (3 different)
#blocks are counterbalanced: One with pictures as primes, one with words as primes.
#It record the latency, response, and correctness
#Saves the data in a way that is appropriate and complete
#Records subject number, age, and gender of the participant
#has a practice trial




#### to strat ####
#import every package in order to run the experiment
from psychopy import visual, core, event, data, gui
import random

##### generate a GUI to ask for participants' information #####
#this comes first that the window, because it doesn't work in full screen
#get some headings in the data
outputFile = open("data.txt", "a")
outputFile.write("{}\t{}\t{}\n".format("Gender", "Age", "ppcode"))
outputFile.close()
#subjects gender and age with GUI
myDlg = gui.Dlg(title="Welcome to the experiment!")
myDlg.addText('Please fill this with your information.')
myDlg.addField('Gender:', choices = ["Male", "Female"])
myDlg.addField('Age:')
myDlg.addField('PPCODE:')
#retrieve data from the participant
ok_data = myDlg.show() 
ppcode = int(myDlg.data[2])
age = myDlg.data[1]
gender = myDlg.data[0]
#right down the data you retrieved
if myDlg.OK:
    outputFile = open("data.txt", "a")
    outputFile.write("{}\t{}\t{}\n".format(ppcode, age, gender))
    outputFile.close()
else:
    outputFile = open("data.txt", "a")
    outputFile.write('user cancelled')
    outputFile.close()




#create a window were everything will be displayed
win = visual.Window(color = "black", fullscr = False)
win.setMouseVisible = False



####trial handler####
# import conditions with trial handler (loading excel files)
conditions = data.importConditions("words.xlsx") #for block 1 
conditions2 = data.importConditions("pics.xlsx") #for block 2
practice = data.importConditions("practice.xlsx") #for practice trials

#create trial handler for block1
nReps = 1
trials = data.TrialHandler(conditions, nReps, method = "fullRandom")
words = visual.TextStim(win)

#creat trial handler for block2
trialspic = data.TrialHandler(conditions2, nReps, method = "fullRandom")
pics = visual.ImageStim(win)
scale = .7
pics.size *= scale / max(pics.size)

#create trial handler for practice trial
trialsprac = data.TrialHandler(practice,nReps, method = "fullRandom")
wordsp = visual.TextStim(win)




####displayed messages####
#create a reminder
reminder = visual.TextStim(win, text = "F is negative       G is positive", pos= (0,-.5), height=.08)
#create feedback for practice trials
feedpos = visual.TextStim(win, text = "You are correct!", pos= (0,0), height=.09, color = "green")
feedneg = visual.TextStim(win, text = "You are incorrect!", pos= (0,0), height=.09, color = "red")
feedno = visual.TextStim(win, text = "You did not respond!", pos= (0,0), height=.09, color = "white")

#add fixation cross
cross = visual.TextStim(win, text = "+")

#get some headings for the next set of info
outputFile = open("data.txt", "a")
outputFile.write("{}\t{}\t{}\t{}\t{}\n".format("prime", "target", "keypress", "RT", "correct"))
outputFile.close()




##### create definitions #####

#for general instructions
def instructions():
    msg = visual.ImageStim(win, image = "C:\Users\s4600479\Desktop//affectiveprime_andrevargas_s4600479//instructions\instructionsg.jpg")
    msg.draw()
    win.flip()
    respond1= event.waitKeys(maxWait=70.0, keyList=["space"]) #press any key to continue or wait 8 secs


#practice trials instructions
def instructionsprac():
    msg = visual.ImageStim(win, image = "C:\Users\s4600479\Desktop//affectiveprime_andrevargas_s4600479//instructions\practice.jpg")
    msg.draw()
    win.flip()
    respond= event.waitKeys(maxWait=70.0, keyList=["space"]) #press any key to continue or wait 8 secs
    msg1 = visual.ImageStim(win, image = "C:\Users\s4600479\Desktop//affectiveprime_andrevargas_s4600479//instructions\practice1.jpg")
    msg1.draw()
    win.flip()
    respond1= event.waitKeys(maxWait=70.0, keyList=["space"]) #press any key to continue or wait 8 secs
    msg2 = visual.ImageStim(win, image = "C:\Users\s4600479\Desktop//affectiveprime_andrevargas_s4600479//instructions\practice2.jpg")
    msg2.draw()
    win.flip()
    respond1= event.waitKeys(maxWait=70.0, keyList=["space"]) #press any key to continue or wait 8 secs
    msg3 = visual.ImageStim(win, image = "C:\Users\s4600479\Desktop//affectiveprime_andrevargas_s4600479//instructions\practice3.jpg")
    msg3.draw()
    win.flip()
    respond1= event.waitKeys(maxWait=70.0, keyList=["space"]) #press any key to continue or wait 8 secs

#create the instructions for block1
def instructions1():
    msg = visual.ImageStim(win, image = "C:\Users\s4600479\Desktop//affectiveprime_andrevargas_s4600479//instructions//block1.jpg")
    msg.draw()
    win.flip()
    respond1= event.waitKeys(maxWait=70.0, keyList=["space"]) #press any key to continue or wait 8 secs

#instructions for block2
def instructions2():
    msg = visual.ImageStim(win, image = "C:\Users\s4600479\Desktop//affectiveprime_andrevargas_s4600479//instructions//block2.jpg")
    msg.draw()
    win.flip()
    respond1= event.waitKeys(maxWait=70.0, keyList=["space"]) #press any key to continue or wait 8 secs

#ending message
def thanks():
    msg = visual.ImageStim(win, image = "C:\Users\s4600479\Desktop//affectiveprime_andrevargas_s4600479//instructions//thanks.jpg")
    msg.draw()
    win.flip()
    respond1= event.waitKeys(maxWait=30.0, keyList=["space"])

#define the whole practice trial
def practice():
    reminder.setAutoDraw(True)
    for trial in trialsprac:
        cross.draw()
        win.flip()
        core.wait(.3)
        wordsp.setText(trial["practicep"])
        wordsp.draw()
        win.flip()
        core.wait(.1)
        cross.draw()
        win.flip()
        core.wait(.1) #draw word prime and cross both for .1 seconds
        wordsp.setText(trial["practicet"])
        wordsp.draw()
        win.flip()
        core.wait(.3) #draw the target word and show it for .3
        cross.draw()
        win.flip()
        clock = core.Clock()
        respond= event.waitKeys(maxWait= 2.6, timeStamped=clock, keyList = ["g", "f"]) #wait for response only with g or f
        #capture response and correctness and give feedback
        if respond:
            respond, latency = respond[0]
            if trial["valence"] == "positive":
                if respond[0][0] == "g":
                    feedpos.draw()
                    win.flip()
                    core.wait(2)
                    response = "correct"
                else:
                    feedneg.draw()
                    win.flip()
                    core.wait(2)
                    response = "incorrect"
            if trial["valence"] == "negative":
                if respond[0][0] == "f":
                    feedpos.draw()
                    win.flip()
                    core.wait(2)
                    response = "correct"
                else:
                    feedneg.draw()
                    win.flip()
                    core.wait(2)
                    response = "incorrect"
        else:
            respond, latency, response = "na", "na","na"
            feedno.draw()
            win.flip()
            core.wait(2)
        cross.draw()
        win.flip()
        core.wait(2.6) #draw the last cross and wait 2.7 + .3 of the starting cross
        win.flip()
    reminder.setAutoDraw(False)

#define block 1 (words as primes)
def block1():
    reminder.setAutoDraw(True)
    for trial in trials:
        cross.draw()
        win.flip()
        core.wait(.3)
        words.setText(trial["Primes"])
        words.draw()
        win.flip()
        core.wait(.1)#and word for .1 second
        cross.draw()
        win.flip()
        core.wait(.1) #draw cross for .1s 
        win.flip()
        words.setText(trial["target"])
        words.draw()
        win.flip()
        core.wait(.3) #draw the target word and show it for .3
        win.flip()
        cross.draw()
        win.flip()
        clock = core.Clock()
        respond= event.waitKeys(maxWait= 2.6, timeStamped=clock, keyList = ["g", "f"]) #wait for response only with g or f
        #capture response and correctness and give feedback
        if respond:
            respond, latency = respond[0]
            if trial["valence"] == "positive":
                if respond[0][0] == "g":
                    response = "correct"
                else:
                    response = "incorrect"
            if trial["valence"] == "negative":
                if respond[0][0] == "f":
                    response = "correct"
                else:
                    response = "incorrect"
        else:
            respond, latency, response = "na", "na","na"
        cross.draw()
        win.flip()
        core.wait(2.6) #draw the last cross and wait 2.7 + .3 of the starting cross
        win.flip()
        #record the generated data of interest
        outputFile = open("data.txt", "a")
        outputFile.write("{}\t{}\t{}\t{}\t{}\n".format(trial["Primes"],trial["target"] ,respond, latency, response))
        outputFile.close()
    reminder.setAutoDraw(False)


#define block 2 (images as primes)
def block2():
    reminder.setAutoDraw(True)
    for trial in trialspic:
        cross.draw()
        win.flip()
        core.wait(.3)
        pics.setImage(trial["Primes"])
        pics.draw()
        win.flip()
        core.wait(.2)#draw pics prime for .2 second
        cross.draw()
        win.flip()
        core.wait(.1) #draw cross for.1 secs
        words.setText(trial["target"])
        words.draw()
        win.flip()
        core.wait(.3) #draw the target word and show it for .3
        cross.draw()
        win.flip()
        clock = core.Clock()
        respond= event.waitKeys(maxWait= 2.6, timeStamped=clock, keyList = ["g", "f"]) #wait for response only with g or f
        #capture response and correctness and give feedback
        if respond:
            respond, latency = respond[0]
            if trial["valence"] == "positive":
                if respond[0][0] == "g":
                    response = "correct"
                else:
                    response = "incorrect"
            if trial["valence"] == "negative":
                if respond[0][0] == "f":
                    response = "correct"
                else:
                    response = "incorrect"
        else:
            respond, latency, response = "na", "na","na"
        cross.draw()
        win.flip()
        core.wait(2.6) #draw the last cross and wait 2.7 + .3 of the starting cross
        win.flip()
        #record the generated data of interest
        outputFile = open("data.txt", "a")
        outputFile.write("{}\t{}\t{}\t{}\t{}\n".format(trial["Primes"],trial["target"] ,respond, latency, response))
        outputFile.close()
    reminder.setAutoDraw(False)




##### experiment order #####
#counterbalance order of blocks and recall all the functions 
#here you can order how the experiment will be displayed as a function of the participant code
if ppcode %2 == 0:
    instructions()
    instructionsprac()
    practice()
    instructions1()
    block1()
    instructions2()
    block2()
    thanks()
else:
    instructions()
    instructionsprac()
    practice()
    instructions2()
    block2()
    instructions1()
    block1()
    thanks()

#close window
win.close()