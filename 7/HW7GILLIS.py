from psychopy import visual, core, event, data, gui
win = visual.Window(color='white')
msg = visual.ImageStim(win, image = "HW7picture.jpg", size = (2, 2))
msg.draw()
win.flip()
respond= event.waitKeys()
color = visual.TextStim(win)

#opening excel
conditions = data.importConditions("HW7_excelfile.xlsx")
trials = data.TrialHandler(conditions, 2, method = 'fullRandom')


#dictionairy

myDlg = gui.Dlg(title="Stroop task")
myDlg.addText('Subject info')
myDlg.addField('Subject number:')
myDlg.addField('Age:')
myDlg.addField('gender', choices= ["Female", "Male"])
ok_data = myDlg.show()  # show dialog and wait for OK or Cancel
if myDlg.OK:  # or if ok_data is not None
    print(ok_data)
else:
    print('user cancelled')





for trial in trials :
    color.setText(trial["colorword"])
    color.setColor(trial["inkcolor"]) 
    color.draw()
    win.flip()
    clock = core.Clock()
    respond= event.waitKeys(timeStamped=clock, keyList = ["r", "b", "o", "y"])
    if trial["inkcolor"] == "red":
        if respond[0][0] == "r":
            response = "correct"
        else:
            response = "incorrect"
            warning = visual.TextStim(win, text="incorrect", color = "black")
            warning.draw()
            win.flip()
    if trial["inkcolor"] == "blue":
        if respond[0][0] == "b":
            response = "correct"
        else:
            response = "incorrect"
            warning = visual.TextStim(win, text="incorrect", color = "black")
            warning.draw()
            win.flip()
    if trial["inkcolor"] == "orange":
        if respond[0][0] == "o":
            response = "correct"
        else:
            response = "incorrect"
            warning = visual.TextStim(win, text="incorrect", color = "black")
            warning.draw()
            win.flip()    
    if trial["inkcolor"] == "yellow":
        if respond[0][0] == "y":
            response = "correct"
        else:
            response = "incorrect"
            warning = visual.TextStim(win, text="incorrect", color = "black")
            warning.draw()
            win.flip()
    core.wait(1)





win.close()