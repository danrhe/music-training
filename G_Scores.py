#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple training for sheets music reading

"""

from expyriment import design, control, stimuli
from settings import *
from ffunctions import *
from expyriment.misc import constants
import random
import numpy as np

# switch off opengl to avoid screen refesh sync
control.defaults.open_gl = False

control.set_develop_mode(True)

exp = design.Experiment(name="G_Scores")

control.initialize(exp)

# Create a canvas and add a clef and white lines to form the music sheet
music_sheet = stimuli.Canvas(settings_canvas['screen_size'], colour=settings_canvas['colour'])

clef = stimuli.Picture('Stimuli/notenschluessel2.jpg',position=[-150, y_init - (2 * line_dist)])
clef.scale(.08)
clef.plot(music_sheet)

lines = createLines()
for item in lines:
    line = stimuli.Line(item['start_point'], item['end_point'], item['line_width'], colour=item['colour'])
    line.plot(music_sheet)

# Create list of Note objects
Notes = []

for item in mapping:
    Notes.append(Note(*item.values()))

random.shuffle(Notes)
control.start()

# Run is created to present more notes than note-objects
nRun = len(Notes)
iRun = 0

for iTrial in range(0, nTrials):

    # Clear the screen
    stimuli.BlankScreen().present(clear=True, update=False)

    # Present the sheet
    music_sheet.present(clear=False, update=True)

    # Add the note to the sheet; if Note needs extra help lines they need to be added first
    if len(Notes[iRun].help_lines) > 0:
        for hline in Notes[iRun].help_lines:
            vals = hline.values()

            help_line = stimuli.Line(hline['start_point'], hline['end_point'], hline['line_width'], colour=hline['colour'])
            help_line.present(clear=False, update=False)

    Notes[iRun].stimuli.present(clear=False, update=True)

    # Wait for button press
    key, rt = exp.keyboard.wait(constants.K_ALL_LETTERS)

    # Evaluate button press
    key_expected = eval("constants.K_" + Notes[iRun].keyboard)

    if isExpectedButton (key, key_expected):
        f = "correct"
        Notes[iRun].RTs = np.append(Notes[iRun].RTs, rt)
        str_rt = str(rt)
    else:
        f = "wrong"
        Notes[iRun].misses += 1
        str_rt = ""

    # Calculate mean RT
    if len(Notes[iRun].RTs) > 0:
        str_mean = str(np.mean(Notes[iRun].RTs))
    else:
        str_mean = ""
    feedback_text = "Type response: " + f + "\nRT: " + str_rt + "\nMean: " + str_mean + "\nMisses: " + str(Notes[iRun].misses)
    feedback = stimuli.TextBox(feedback_text, [400, 400], position=[0, (y_init - (15 * line_dist))], text_size=24)
    feedback.present(clear=False, update=True)


    # Add feedback to the screen
    text_mapping = stimuli.TextBox(Notes[iRun].key, [100, 100], position=[0, (y_init - (6 * line_dist))], text_size=24)
    text_mapping.present(clear=False, update=True)
    exp.keyboard.wait(constants.K_SPACE)

    # Check if all notes have been shown. If not, increase index, otherwise shuffle notes and begin again
    if iRun < (nRun - 1):
        iRun += 1
    else:
        random.shuffle(Notes)
        iRun = 0

control.end(goodbye_text='Thats it', goodbye_delay=1000)

