#!/usr/bin/env python
# -*- coding: utf-8 -*-

from expyriment import stimuli
from settings import *
import numpy as np


class Note:
    """
    :param: position on screen, name of the note, associated keyboard key, color

    """

    def __init__(self, position_factor, key, keyboard='K_SPACE', colour=None):

        if colour is not None:
            self.colour = colour
        else:
            self.colour = white

        # Assign
        self.key = key
        self.position_factor = position_factor
        self.position_y = y_init + (position_factor * line_dist / 2)
        self.position = [0, self.position_y]

        self.keyboard = keyboard

        # standard values for each note
        self.size = [line_dist, line_dist / 2]
        self.stimuli = stimuli.Ellipse(self.size, colour=self.colour, position=self.position)

        self.count = 0
        self.RTs = np.array([])
        self.misses = 0

        # Parameter for help lines outsite five music sheet lines
        self.help_lines = list()
        if self.position_factor <= -6:
            # range (a,b) needs to have a lower b to initiate array with first element
            for line in range (-6, self.position_factor -1, -2):
                self.help_lines.append({
                    'start_point': [-1.2 * line_dist, y_init + (line * line_dist / 2)],
                    'end_point': [1.2 * line_dist, y_init + (line * line_dist / 2)],
                    'line_width': 3,
                    'colour': white,
                })
        else:
            if self.position_factor >= 6:
                # range (a,b) needs to have a lower b to initiate array with first element
                for line in range (6, self.position_factor +1, 2):
                    self.help_lines.append({
                        'start_point': [-1.2 * line_dist, y_init + (line * line_dist / 2)],
                        'end_point': [1.2 * line_dist, y_init + (line * line_dist / 2)],
                        'line_width': 3,
                        'colour': white,
                    })

def isExpectedButton (expectedButton, actualPressedButton):

    if expectedButton == actualPressedButton:
        return True
    else:
        return False

def createLines(midline=y_init, distance=line_dist):
    """
    Creates Parameters for music sheet lines
    """
    lines = list()
    for i in range(-2, 3, 1):
        lines.append(
            {
            'start_point': [-110, midline - (i * distance)],
            'end_point': [110, midline - (i * distance)],
            'line_width': 3,
            'colour': white,
            })
    return lines



