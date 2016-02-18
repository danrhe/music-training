"""
Music Training Settings.

This module contains a class implementing all training settings.

"""

__author__ = 'Daniel von Rhein <Daniel.vonRhein@gmail.com>'
__version__ = '0.1.0'
__date__ = 'Tue Feb 18 10:14:58 2016 +0200'


class Settings:
    """A class implementing all settings.
    @:param screen_size list with screen resolution

    """

    def __init__(self, screen_size):

        self.white = [255, 255, 255]
        self.black = [0, 0, 0]
        self.nTrials = 100

        self.OPTIONS = {"Design": 1,
           "clef": ["g", "f"],
           "black_keys": False,
           "all_notes_once": True,
           "colour": "bw"
           }

        self.settings_canvas = {
            'screen_size': screen_size,
            'colour': self.black,
            }

        self.settings_feedback = {
            "size_box": [self.settings_canvas['screen_size'][0] /4, self.settings_canvas['screen_size'][1] /4],
            "position": [0, 0 - (self.settings_canvas['screen_size'][1] /4)],
            "text_size": 24,
            }

        self.settings_correctnote = {
            "size_box": [self.settings_canvas['screen_size'][0] /4, self.settings_canvas['screen_size'][1] /4],
            "position": [0, 0 - (self.settings_canvas['screen_size'][1] /2)],
            "text_size": 24,
        }

        # position of the stimuli relative to screen size
        self.y_init = self.settings_canvas['screen_size'][1] / 7
        self.line_dist = self.settings_canvas['screen_size'][1] / 100

        self.mapping = [
            {'key': 'c3',
             'position_factor': 8,
             'keyboard': 'c',
             'clef': 'g'
             },
            {'key': 'b2',
             'position_factor': 7,
             'keyboard': 'b',
             'clef': 'g'
             },
            {'key': 'a2',
             'position_factor': 6,
             'keyboard': 'a',
             'clef': 'g'
             },
            {'key': 'g2',
             'position_factor': 5,
             'keyboard': 'g',
             'clef': 'g'
             },
            {'key': 'f2',
             'position_factor': 4,
             'keyboard': 'f',
             'clef': 'g'
             },
            {'key': 'e2',
             'position_factor': 3,
             'keyboard': 'e',
             'clef': 'g'
             },
            {'key': 'd2',
             'position_factor': 2,
             'keyboard': 'd',
             'clef': 'g'
             },
            {'key': 'c2',
             'position_factor': 1,
             'keyboard': 'c',
             'clef': 'g'
             },
            {'key': 'b1',
             'position_factor': 0,
             'keyboard': 'b',
             'clef': 'g'
             },
            {'key': 'a1',
             'position_factor': -1,
             'keyboard': 'a',
             'clef': 'g'
             },
            {'key': 'g1',
             'position_factor': -2,
             'keyboard': 'g',
             'clef': 'g'
             },
            {'key': 'f1',
             'position_factor': -3,
             'keyboard': 'f',
             'clef': 'g'
             },
            {'key': 'e1',
             'position_factor': -4,
             'keyboard': 'e',
             'clef': 'g'
             },
            {'key': 'd1',
             'position_factor': -5,
             'keyboard': 'd',
             'clef': 'g'
             },
            {'key': 'c1',
             'position_factor': -6,
             'keyboard': 'c',
             'clef': 'g'
             },
            {'key': 'b',
             'position_factor': -7,
             'keyboard': 'b',
             'clef': 'g'
             },
            {'key': 'a',
             'position_factor': -8,
             'keyboard': 'a',
             'clef': 'g'
             },
            {'key': 'e',
             'position_factor': 8,
             'keyboard': 'e',
             'clef': 'f'
             },
            {'key': 'd',
             'position_factor': 7,
             'keyboard': 'd',
             'clef': 'f'
             },
            {'key': 'c',
             'position_factor': 6,
             'keyboard': 'c',
             'clef': 'f'
             },
            {'key': 'b',
             'position_factor': 5,
             'keyboard': 'b',
             'clef': 'f'
             },
            {'key': 'a',
             'position_factor': 4,
             'keyboard': 'a',
             'clef': 'f'
             },
            {'key': 'g',
             'position_factor': 3,
             'keyboard': 'g',
             'clef': 'f'
             },
            {'key': 'f',
             'position_factor': 2,
             'keyboard': 'f',
             'clef': 'f'
             },
            {'key': 'e',
             'position_factor': 1,
             'keyboard': 'e',
             'clef': 'f'
             },
            {'key': 'd',
             'position_factor': 0,
             'keyboard': 'd',
             'clef': 'f'
             },
            {'key': 'c',
             'position_factor': -1,
             'keyboard': 'c',
             'clef': 'f'
             },
            {'key': 'B',
             'position_factor': -2,
             'keyboard': 'b',
             'clef': 'f'
             },
            {'key': 'A',
             'position_factor': -3,
             'keyboard': 'a',
             'clef': 'f'
             },
            {'key': 'G',
             'position_factor': -4,
             'keyboard': 'g',
             'clef': 'f'
             },
            {'key': 'F',
             'position_factor': -5,
             'keyboard': 'f',
             'clef': 'f'
             },
            {'key': 'E',
             'position_factor': -6,
             'keyboard': 'e',
             'clef': 'f'
             },
            {'key': 'D',
             'position_factor': -7,
             'keyboard': 'd',
             'clef': 'f'
             },
            {'key': 'C',
             'position_factor': -8,
             'keyboard': 'c',
             'clef': 'f'
             },

        ]
