#!/usr/bin/env python
# -*- coding: utf-8 -*-
from expyriment import stimuli
import numpy as np
from expyriment.misc import constants


class Note:
    """
    :param: position on screen, name of the note, associated keyboard key, color

    """

    def __init__(self, position_factor, clef, key, keyboard, colour, midline, distance):

        # Assign
        self.colour = colour
        self.key = key
        self.clef = clef
        self.position_factor = position_factor
        self.position_y = midline + (position_factor * distance / 2)
        self.position = [0, self.position_y]

        self.keyboard = keyboard

        # standard values for each note
        self.size = [distance, distance / 2]
        self.stimuli = stimuli.Ellipse(self.size, colour=self.colour, position=self.position)

        self.count = 0
        self.RTs = np.array([])
        self.misses = 0

        # Parameter for help lines outside five music sheet lines
        self.help_lines = list()
        if self.position_factor <= -6:
            # range (a,b) needs to have a lower b to initiate array with first element
            for line in range (-6, self.position_factor -1, -2):
                self.help_lines.append({
                    'start_point': [-1.2 * distance, midline + (line * distance / 2)],
                    'end_point': [1.2 * distance, midline + (line * distance / 2)],
                    'line_width': 1,
                    'colour': self.colour,
                })
        else:
            if self.position_factor >= 6:
                # range (a,b) needs to have a lower b to initiate array with first element
                for line in range (6, self.position_factor +1, 2):
                    self.help_lines.append({
                        'start_point': [-1.2 * distance, midline + (line * distance / 2)],
                        'end_point': [1.2 * distance, midline + (line * distance / 2)],
                        'line_width': 2,
                        'colour': self.colour,
                    })

def isExpectedButton (expectedButton, actualPressedButton):

    if expectedButton == actualPressedButton:
        return True
    else:
        return False

def createLineParameter(midline, distance, design):
    """
    Creates Parameters for music sheet lines
    """
    lines = list()

    if design == 'wb':
        colour = constants.C_WHITE
    else:
        colour = constants.C_BLACK

    for i in range(-2, 3, 1):
        lines.append(
            {
            'start_point': [-110, midline - (i * distance)],
            'end_point': [110, midline - (i * distance)],
            'line_width': 3,
            'colour': colour
            })
    return lines



def createMusicSheet(clef_name, lines, settings_field, screen_size, design, y_init, line_dist):
    """
    Creates music sheet with clef and horizontal lines
    """

    if design == "bw":
        colour = (0, 0, 0)
    else:
        colour = (255, 255, 255)

    new_sheet = stimuli.Canvas(screen_size, colour=colour)

    # Add field for black on white
    f = 4
    field_x = settings_field._window_size[0] / f
    field_y = settings_field._window_size[1] / f
    pos_x = 0
    pos_y = field_y / 2



    field = stimuli.Canvas([field_x, field_y], position=[pos_x, pos_y ] ,colour=constants.C_WHITE)
    field.plot(new_sheet)
    # Add clef
    clef = stimuli.Picture('Stimuli/clef_' + design + '_' + clef_name + '.jpg', position=[-150, y_init - (0 * line_dist)])
    clef.scale(.02)
    clef.plot(new_sheet)

    # Add 5 lines
    for item in lines:
        line = stimuli.Line(item['start_point'], item['end_point'], item['line_width'], colour=item['colour'])
        line.plot(new_sheet)

    return new_sheet





