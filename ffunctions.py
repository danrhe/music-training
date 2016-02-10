#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""


"""
from expyriment import stimuli
from settings import *
import numpy as np


class Note:

    def __init__(self, position, key, keyboard='K_SPACE', colour=None):

        if colour is not None:
            self.colour = colour
        else:
            self.colour = white

        # Assign
        self.key = key
        self.position = position
        self.keyboard = keyboard

        # standard values for each note
        self.size = [line_dist, line_dist / 2]
        self.stimuli = stimuli.Ellipse(self.size, colour=self.colour, position=self.position)

        self.count = 0
        self.RTs = np.array([])
        self.misses = 0


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



