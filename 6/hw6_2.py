#20 trials done
#5 males names done
#5 female names done
#use twice each done
#one list with all names done
#random.shuffle() to randomize the order done
#then loop through the list done
#one line of instruction before the task starts done
#record responce and latency
#save: trial number, presented stimuli, response, and latency to a txt file, one row per response

from psychopy import visual, core, event
import random
win = visual.Window()
msg = visual.TextStim(win, text="press f if female m if male")
reminder = visual.TextStim(win, text = "press f if female m if male", units = "norm",pos=(0,.5))
msg.draw()
win.flip()
respond1= event.waitKeys(maxWait=6.0)
names = ["Thijs", "Johanes", "Jonnas", "Julian", "Krisna", "Melanie", "Martje", "Sarah", "Ana", "Samy"]
random.shuffle(names)
print(names) 
trial=0
outputFile = open("data.txt", "a")
outputFile.write("{}\t{}\t{}\t{}\n".format("response", "latency", "trial", "stimuli"))
outputFile.close()
for i in (names*2):
    trial = trial+ 1
    msg = visual.TextStim(win, text=i)
    msg.draw()
    reminder.draw()
    win.flip()
    clock = core.Clock()
    respond= event.waitKeys(maxWait=6.0, timeStamped=clock) 
    if respond:
        response, latency = respond[0]
    else:
        response, latency = "na", "na"
    outputFile = open("data.txt", "a")
    outputFile.write("{}\t{}\t{}\t{}\n".format(response, latency, trial, i))
    outputFile.close()
win.close() 