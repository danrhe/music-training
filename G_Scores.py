#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple training for sheets music reading

"""

from expyriment import design, control, io
from ffunctions import *
from expyriment.misc import constants
import random
import numpy as np

# switch off opengl to avoid screen refesh sync
control.defaults.open_gl = False

# control.set_develop_mode(True)

exp = design.Experiment(name="MusicTraining")

control.initialize(exp)
#io.DataFile
options = {"Design": 1,
           "clef": ["f"],
           "black_keys": False,
           "all_notes_once": True,
           "color": "wb"
           }

# setupTraining(options)

# Create one ore more canvas and add a clef and white lines to form the music sheet
music_sheet = dict()

for clef in options['clef']:
    music_sheet[clef] = createMusicSheet(clef)


lines = createLines()
for item in lines:
    line = stimuli.Line(item['start_point'], item['end_point'], item['line_width'], colour=item['colour'])

    for clef in options['clef']:
        line.plot(music_sheet[clef])

# Create list of Note objects
Notes = []

# get notes with certain characteristics
selection = [x for x in mapping if x['clef'] in options['clef']]

for item in selection:
    Notes.append(Note(*item.values()))

random.shuffle(Notes)
control.start(subject_id=25)

# Add variable header to data_file
exp._data.add_variable_names(["Trial", "clef", "key", "Expected", "Type_response", "RT"])

# Run is created to present more notes than note-objects
nRun = len(Notes)
iRun = 0

for iTrial in range(0, nTrials):

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
    feedback_text = "Type response: " + f + "\nRT: " + str_rt + "\nMean: " + str_mean + "\nMisses: " + str(Notes[iRun].misses)
    feedback = stimuli.TextBox(feedback_text, [400, 400], position=[0, (y_init - (15 * line_dist))], text_size=24)
    feedback.present(clear=False, update=True)


    # Add feedback to the screen
    text_mapping = stimuli.TextBox(Notes[iRun].key, [100, 100], position=[0, (y_init - (7 * line_dist))], text_size=24)
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

