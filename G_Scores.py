#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple training for sheets music reading

"""

from expyriment import design, control, stimuli
from settings import *
from expyriment.misc import constants
import random
control.defaults.open_gl = False # switch off opengl to avoid screen refesh sync
control.set_develop_mode(True)

exp = design.Experiment(name="G_Scores")
control.initialize(exp)


nTrials = 5

# Create a canvas and add a clef and white lines to form the music sheet
music_sheet = stimuli.Canvas(settings_canvas['screen_size'], colour=settings_canvas['colour'])

clef = stimuli.Picture('Stimuli/notenschluessel2.jpg',position=[-150, y_init - (2 * line_dist)])
clef.scale(.08)
clef.plot(music_sheet)

for item in lines:
    line = stimuli.Line(item['start_point'],
                    item['end_point'],
                    item['line_width'],
                    colour=item['colour'])
    line.plot(music_sheet)


notes = []

for item in mapping:
    notes.append(Note(*item.values()))

control.start()


for iTrial in range(0, nTrials):

    # get the index of one note - key mapping ; keep in mind that index starts with 0, thus last index is len - 1
    iNote = random.randint(0, (len(notes)-1))


    # Clear the screen
    stimuli.BlankScreen().present(clear=True, update=False)

    # Present the sheet
    music_sheet.present(clear=False, update=True)

    # Add the note to the sheet
    notes[iNote].stimuli.present(clear=False, update=True)


    # Wait for button press
    exp.keyboard.wait(eval("constants.K_" + notes[iNote].keyboard))

    # Add feedback to the screen
    text_mapping = stimuli.TextBox(notes[iNote].key, [100, 100], position=[0, (y_init - (7 * line_dist))], text_size=24)
    text_mapping.present(clear=False,update=True)
    exp.keyboard.wait(constants.K_SPACE)

control.end(goodbye_text='Thats it', goodbye_delay=1000)

