from expyriment import design, control,stimuli
from expyriment.misc import constants
from functions2 import MusicSheet, Notes, Feedback, CorrectNote
from settings import Setup
import random
'''
Custom settings
'''
# switch off opengl to avoid screen refesh sync
control.defaults.open_gl = False

# Fast open close and windowed; default: False
control.set_develop_mode(True)
#control.defaults.initialize_delay = 0

'''
Prepare Training
'''
#Initialize experiment and load setup
exp = design.Experiment(name="MusicTraining")
control.initialize(exp)
setup = Setup(screen_size=exp.screen.size)

# Create list of musicsheet objects
musicsheet = dict()
for clef in setup.clef:
    musicsheet[clef] = MusicSheet(screen_size=exp.screen.size, pos_y=setup.pos_y, clef_name=clef)

# Create list of note objects
Notes = Notes(setup.clef, setup.pos_y, setup.distance)

#Randomize order of notes
random.shuffle(Notes.selection)


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

    musicsheet[Notes.selection[iRun].clef].Field.present(clear=False, update=True)

    # Add the note to the sheet; if Note needs extra help lines they need to be added first
    if len(Notes.selection[iRun].help_lines) > 0:
        for hline in Notes.selection[iRun].help_lines:
            vals = hline.values()

            help_line = stimuli.Line(hline['start_point'], hline['end_point'], hline['line_width'], colour=hline['colour'])
            help_line.present(clear=False, update=False)

    Notes.selection[iRun].stimuli.present(clear=False, update=True)

    # Wait for button press
    key, rt = exp.keyboard.wait(constants.K_ALL_LETTERS)

    # Evaluate button press
    Notes.selection[iRun].Evaluate_Buttonpress(key, rt)

    # Add feedback and correct note to the screen
    fb = Feedback(note=Notes.selection[iRun], settings=setup.settings_feedback)
    cn = CorrectNote(note=Notes.selection[iRun], settings=setup.settings_correctnote)

    fb.TextBox.present(clear=False, update=False)
    cn.CorrectNote.present(clear=False, update=True)

    exp.keyboard.wait(constants.K_SPACE)

    exp._data.add([iTrial, Notes.selection[iRun].clef, Notes.selection[iRun].key, Notes.selection[iRun].key_coded, Notes.selection[iRun].Feedback_text, rt])

    if iRun < (len(Notes.selection)-1):
        iRun += 1
    else:
        random.shuffle(Notes)
        iRun = 0

control.end(goodbye_text='Thats it', goodbye_delay=1000)