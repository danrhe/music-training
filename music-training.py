from expyriment import design, control,stimuli
from expyriment.misc import constants
from functions2 import MusicSheet, Notes
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
Prepare experiment
'''

exp = design.Experiment(name="MusicTraining")

control.initialize(exp)
setup = Setup(screen_size=exp.screen.size)

# Create list of musicsheet objects
musicsheet = dict()
for clef in setup.clef:
    musicsheet[clef] = MusicSheet(screen_size=exp.screen.size, pos_y=setup.pos_y, clef_name=clef)

# Create list of note objects
Notes = Notes(setup.clef, setup.pos_y, setup.distance)

random.shuffle(Notes.selection)

control.start(subject_id=45)

# Add variable header to data_file
exp._data.add_variable_names(["Trial", "clef", "key", "Expected", "Type_response", "RT"])


# Run is created to present more notes than note-objects
nRun = len(Notes.selection)
iRun = 0

'''
Trial function
'''

stimuli.BlankScreen().present(clear=True, update=False)

musicsheet[Notes.selection[iRun].clef].Field.present(clear=False, update=True)

# Wait for button press
key, rt = exp.keyboard.wait(constants.K_ALL_LETTERS)

# Add the note to the sheet; if Note needs extra help lines they need to be added first
if len(Notes.selection[iRun].help_lines) > 0:
    for hline in Notes.selection[iRun].help_lines:
        vals = hline.values()

        help_line = stimuli.Line(hline['start_point'], hline['end_point'], hline['line_width'], colour=hline['colour'])
        help_line.present(clear=False, update=False)

Notes.selection[iRun].stimuli.present(clear=False, update=True)

# Wait for button press
key, rt = exp.keyboard.wait(constants.K_ALL_LETTERS)

control.end(goodbye_text='Thats it', goodbye_delay=1000)