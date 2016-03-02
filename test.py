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


rect = stimuli.Rectangle([20,40],[200,0,0], position=[20,20])

control.start(subject_id=45)

stimuli.BlankScreen().present(clear=True, update=False)

rect.present(clear=False, update=True)
mouse = io.Mouse()
mouse.show_cursor()

for i in range(0, 10000):

    position = rect.position
    size = rect.size

    mp = mouse.position

    right = (size[0] / 2) + position[0]
    left = right - size[0]
    top = (size[1] / 2) + position[1]
    bottom = top - size[1]

    if mp[0] <= right and mp[0] >=  left and mp[1] <= top and mp[1] >= bottom:
        t = 'TRUE'
    else:
        t = 'FALSE'

    text = stimuli.TextLine(t, [0,-100], text_colour=[200,200,0])
    text2 = stimuli.TextLine("R: " + str(right) + " L: " + str(left) + " T: " + str(top) + "B: " + str(bottom), [0,-150], text_colour=[200,200,0])
    text3 = stimuli.TextLine("mp[0]: " + str(mp[0]) + " mp[1]: " + str(mp[1]), [0,-200], text_colour=[200,200,0])


    text.present(clear=True, update=False )
    text2.present(clear=False, update=False )
    text3.present(clear=False, update=False )
    rect.present(clear=False, update=True)


# Wait for button press
key, rt = exp.keyboard.wait(constants.K_ALL_LETTERS)


control.end(goodbye_text='Thats it', goodbye_delay=1000)