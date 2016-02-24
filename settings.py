"""
Music Training Settings.

This module contains a class implementing all training settings.

"""

__author__ = 'Daniel von Rhein <Daniel.vonRhein@gmail.com>'
__version__ = '0.1.0'
__date__ = 'Tue Feb 18 10:14:58 2016 +0200'

# dictionary with several setting

class Setup:
    """A class implementing all settings.
    @:param screen_size list with screen resolution
    # Create line parameters
    lines = createLineParameter(set.y_init, set.line_dist, set.OPTIONS['colour'])
    """
    def __init__(self, screen_size):
        self.nTrials = 2
        self.clef = ["g", "f"]
        self.black_keys = False
        self.all_notes_once = True
        self.colour = "bw"
        self.pos_y = {
            "g": 0 + screen_size[1] / 4,
            "f": 0 + screen_size[1] / 4
            }

        self.distance = screen_size[0] / 60

        self.settings_feedback = {
            "size_box": [screen_size[0] /4, screen_size[1] /4],
            "position": [0, 0 - (screen_size[1] /4)],
            "text_size": 24,
            }

        self.settings_correctnote = {
            "size_box": [screen_size[0] /4, screen_size[1] /4],
            "position": [0, 0],
            "text_size": 34,
            }

        # position of the stimuli relative to screen size
        self.y_init = screen_size[1] / 7
        self.line_dist = screen_size[1] / 100

