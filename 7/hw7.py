#Program a Stroop task 
#32 trials: 4 ink colors x 4 color names x 2 presentations 
#Task: name the ink the stimulus is written in, possible responses are the 4 color names (so use four different keys)
#Use TrialHandler to load conditions, randomize and run the trials, and save the data
#Display instructions using ImageStims
#Give error feedback when subject makes a mistake
#Save trial number, ink color of the stimulus, color name of the stimulus, response, latency, whether the response is correct (note: some of these will be saved automatically with TrialHandler!) to a text or excel file
#Also save subject number, subject age, and subject gender

from psychopy import visual, core, event, data, gui
import random
win = visual.Window()
msg = visual.ImageStim(win, image = "C:\Users\s4600479\Desktop\instructions.jpg")
msg.draw()
win.flip()
respond1= event.waitKeys(maxWait=6.0)

#feedback

feed = visual.TextStim(win, text = "wrong response")

#subjects gender and age
myDlg = gui.Dlg(title="experiment")
myDlg.addText('Subject info')
myDlg.addField('Gender:', choices = ["male", "female"])
myDlg.addField('Age:')
myDlg.addField('PPCODE:')
ok_data = myDlg.show() 
ppcode = myDlg.data[2]
age = myDlg.data[1]
gender = myDlg.data[0]
if myDlg.OK:  # or if ok_data is not None
    outputFile = open("data.txt", "a")
    outputFile.write("{}\t{}\t{}\n".format(ppcode, age, gender))
    outputFile.close()
else:
    outputFile = open("data.txt", "a")
    outputFile.write('user cancelled')
    outputFile.close()
# import conditions
conditions = data.importConditions("Book1.xlsx")

#create trial handler
nReps = 2
trials = data.TrialHandler(conditions, nReps, method = "fullRandom")
colorwords = visual.TextStim(win)

n = 0

for trial in trials:
    n = n + 1
    word = colorwords.setText(trial.get("word"))
    ink = colorwords.setColor(trial.get("ink"))
    colorwords.draw()
    responds= event.waitKeys(maxWait=1.0)
    win.flip()
    clock = core.Clock()
    respond= event.waitKeys(maxWait= 2.0, timeStamped=clock, keyList = ["r", "b", "g", "y"]) 
    if respond:
        respond, latency = respond[0]
        if trial["ink"] == "blue":
            if respond[0][0] == "b":
                response = "correct"
            else:
                response = "incorrect"
                feed.draw()
                win.flip()
                core.wait(1)
        if trial["ink"] == "yellow":
            if respond[0][0] == "y":
                response = "correct"
            else:
                response = "incorrect"
                feed.draw()
                win.flip()
                core.wait(1)
        if trial["ink"] == "green":
            if respond[0][0] == "g":
                response = "correct"
            else:
                response = "incorrect"
                feed.draw()
                win.flip()
                core.wait(1)
        if trial["ink"] == "red":
            if respond[0][0] == "r":
                response = "correct"
            else:
                response = "incorrect"
                feed.draw()
                win.flip()
                core.wait(1)
    else:
        respond, latency, response = "na", "na", 'na'
    print trial["word"], trial["ink"], trial
    outputFile = open("data.txt", "a")
    outputFile.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(n, trial["word"],trial["ink"] ,respond, latency, response))
    outputFile.close()
win.close() 