from expyriment import design, control, stimuli, io
from expyriment.misc import constants
from musicsheet import MusicSheet, Notes, Feedback
from settings import Setup
from keyboard import PianoKeyboard
import random
from mysql import *
'''
Custom settings
'''
# switch off opengl to avoid screen refresh sync
control.defaults.open_gl = False

# Fast open close and windowed; default: False
control.set_develop_mode(True)
io.defaults.outputfile_time_stamp = True
#control.defaults.initialize_delay = 0


'''
Prepare Training
'''
#Initialize experiment and load setup
exp = design.Experiment(name="MusicTraining")
control.initialize(exp)
setup = Setup(screen_size=exp.screen.size, use_all_notes=True)
exp.mouse.show_cursor()

# Create list of musicsheet objects
musicsheet = dict()
for clef in setup.clef:
    musicsheet[clef] = MusicSheet(screen_size=exp.screen.size, pos_y=setup.pos_y, clef_name=clef)

# Create list of note objects
Notes = Notes()
Notes.appendnotes(setup.selection, setup.pos_y, setup.distance)

# Create Piano keyboard on screen
piano = PianoKeyboard(exp.screen.size)


#Randomize order of notes
random.shuffle(Notes)


'''
Start Training
'''
control.start(subject_id=45)

# Add variable header to data_file; can't be done before control.start
exp._data.add_variable_names(["Trial", "clef", "key", "Expected", "Type_response", "RT"])

# iRun indexes the Notes array; when all notes are shown and nTrails remain, this index is set to 0 and runs again
iRun = 0

'''
Trial function
'''
for iTrial in range(0, setup.nTrials):

    stimuli.BlankScreen().present(clear=True, update=False)

    piano.Canvas.present(clear=False, update=False)

    # Present empty music sheet
    musicsheet[Notes[iRun].clef].Field.present(clear=False, update=True)

    # if Note needs extra help lines they need to be added first
    musicsheet[Notes[iRun].clef].add_helplines(Notes[iRun])

    # if Note has prefix, add it to screen
    musicsheet[Notes[iRun].clef].add_prefix(Notes[iRun])

    # Present note, prefix and lines
    Notes[iRun].stimuli.present(clear=False, update=True)

    # Wait for button press
    key, rt = exp.keyboard.wait(constants.K_SPACE, 8000)

    if key is None:
        key = constants.K_q
        rt = 8000

    mp = exp.mouse.position

    #index pressed key
    index = piano.findKey(Notes[iRun].nid)

    # Evaluate mouse position
    piano.evalMouse(index, mp)

    # Evaluate button press
    Notes[iRun].Evaluate_Buttonpress(key, rt, piano.MouseBool)


    # Add feedback about performance and correct key to the screen
    fb = Feedback(note=Notes[iRun], settings=setup.settings_feedback)
    fb.TextBox.present(clear=False, update=False)


#    text = stimuli.TextLine(str(piano.MouseBool), [0,-100], text_colour=[200,200,0])
#    text.present(clear=True, update=False)

    piano.printColoredKey(index)
    piano.printKeyName(index, Notes[iRun].name)

    exp.keyboard.wait(constants.K_SPACE)

    exp._data.add([iTrial, Notes[iRun].clef, Notes[iRun].key, Notes[iRun].key_coded, Notes[iRun].Feedback_text, rt])

    if iRun < (len(Notes)-1):
        iRun += 1
    else:
        random.shuffle(Notes)
        iRun = 0

control.end(goodbye_text='Thats it', goodbye_delay=1000)
#write_to_MySQL()
