#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple training for sheets music reading

"""
"""
Import Contributed packages
"""
from expyriment import design, control
import random
import numpy as np

'''
Custom settings
'''
# switch off opengl to avoid screen refesh sync
control.defaults.open_gl = False

# Fast open close and windowed; default: False
#control.set_develop_mode(True)

'''
Prepare experiment
'''
exp = design.Experiment(name="MusicTraining")
control.initialize(exp)

from settings import Settings

set = Settings([1680,1050])


# Create line parameters
from functions import *
lines = createLineParameter(set.y_init, set.line_dist, set.OPTIONS['colour'])

music_sheet = dict()

for clef in set.OPTIONS['clef']:
    music_sheet[clef] = createMusicSheet(clef, lines, exp.screen,set.settings_canvas['screen_size'], set.OPTIONS['colour'], set.y_init, set.line_dist)

# Create list of note objects
Notes = []

# get notes with certain characteristics
selection = [x for x in set.mapping if x['clef'] in set.OPTIONS['clef']]

for item in selection:
    vals = item.values()
    vals.extend([constants.C_BLACK, set.y_init, set.line_dist])
    Notes.append(Note(*vals))

random.shuffle(Notes)
control.start(subject_id=25)

# Add variable header to data_file
exp._data.add_variable_names(["Trial", "clef", "key", "Expected", "Type_response", "RT"])

# Run is created to present more notes than note-objects
nRun = len(Notes)
iRun = 0

'''
Trial function
'''
for iTrial in range(0, set.nTrials):

    # Clear the screen
    stimuli.BlankScreen().present(clear=True, update=False)

    # Present the sheet
    music_sheet[Notes[iRun].clef].present(clear=False, update=True)

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

    # Add feedback to the screen
    feedback_text = "Type response: " + f + "\nRT: " + str_rt + "\nMean: " + str_mean + "\nMisses: " + str(Notes[iRun].misses)
    tbox_feedback = stimuli.TextBox(feedback_text, set.settings_feedback["size_box"],set.settings_feedback["position"],text_size=set.settings_feedback["text_size"])
    tbox_feedback.present(clear=False, update=True)


    # Add correct note to the screen
    text_mapping = stimuli.TextBox(Notes[iRun].key, set.settings_correctnote["size_box"],set.settings_correctnote["position"],text_size=set.settings_correctnote["text_size"])
    text_mapping.present(clear=False, update=True)
    exp.keyboard.wait(constants.K_SPACE)

    # Export data
    exp._data.add([iTrial, Notes[iRun].clef, Notes[iRun].key, key_expected, f, rt])
    # Check if all notes have been shown. If not, increase index, otherwise shuffle notes and begin again
    if iRun < (nRun - 1):
        iRun += 1
    else:
        random.shuffle(Notes)
        iRun = 0

control.end(goodbye_text='Thats it', goodbye_delay=1000)

