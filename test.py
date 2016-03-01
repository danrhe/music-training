from expyriment import design, control,stimuli,io
from expyriment.misc import constants
from functions2 import MusicSheet
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


musicsheet = MusicSheet(screen_size=exp.screen.size, pos_y={'g': 0, 'f': 0})

control.start(subject_id=45)

stimuli.BlankScreen().present(clear=True, update=False)

musicsheet.Field.present(clear=False, update=True)
mouse = io.Mouse()
mouse.show_cursor()
# Wait for button press
key, rt = exp.keyboard.wait(constants.K_ALL_LETTERS)


control.end(goodbye_text='Thats it', goodbye_delay=1000)