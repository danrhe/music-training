from note_info import note_mapping
from use_user_history import User_data
from mysql import *

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
        self.nTrials = 50 # one set
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
            "position": [-200, 0 - (screen_size[1] /4)],
            "text_size": 24,
            }

        self.settings_correctnote = {
            "size_box": [screen_size[0] /4, screen_size[1] /4],
            "position": [0, -200],
            "text_size": 40,
            }

        # position of the stimuli relative to screen size
        self.y_init = screen_size[1] / 7
        self.line_dist = screen_size[1] / 100

    def make_selection(self, use_all_notes=False, refresh_user_data=True):

        self.refresh_user_data = refresh_user_data
        self.use_all_notes = use_all_notes

        self.all_notes = [x for x in note_mapping if x['clef'] in self.clef]

        if self.use_all_notes:
                self.selection = self.all_notes

        else:
            try:
                u = User_data('45')
                u.get_data(self.refresh_user_data)
                u.calc_hitrate()
                u.get_bad_performance()
                u.make_selection(self.all_notes)
                self.selection = u.selection
            except:
                print ('Couldn\'t load user data')
                print ('using all notes')
                self.selection = self.all_notes
            else:
                print ('Using only notes with poor user performance')
                return u




        #self.selection = [x for x in note_mapping if x['key'] is 'Db']
        #self.selection = [x for x in note_mapping if x['pid'] is '100']

