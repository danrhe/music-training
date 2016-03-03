from expyriment import design, control,stimuli,io
from expyriment.misc import constants
from functions2 import MusicSheet, mouseIsInside
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


rect = stimuli.Rectangle([80,20],[200,0,0], position=[120,-30])

control.start(subject_id=45)

stimuli.BlankScreen().present(clear=True, update=False)

rect.present(clear=False, update=True)
mouse = io.Mouse()
mouse.show_cursor()

for i in range(0, 1000):

    t = mouseIsInside(rect.size, rect.position, mouse.position)

    text = stimuli.TextLine(t, [0,-100], text_colour=[200,200,0])


    text.present(clear=True, update=False )
    rect.present(clear=False, update=True)


# Wait for button press
key, rt = exp.keyboard.wait(constants.K_ALL_LETTERS)


control.end(goodbye_text='Thats it', goodbye_delay=1000)