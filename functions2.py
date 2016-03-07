from expyriment import stimuli
from expyriment.misc import constants
import numpy as np

class MusicSheet:
    """
    Creates music sheet. This is a composite of white canvas field) with clef and horizontal lines
    """
    def __init__(self, screen_size,  pos_y, clef_name="g", design="bw", text=None):

        self.background_colour = constants.C_WHITE
        self.foreground_colour = constants.C_BLACK
        self.clef_name = clef_name

        # Position of field
        self.pos_x = 0
        self.pos_y = pos_y[self.clef_name]

        self.field_position = [self.pos_x, self.pos_y]

        # Size of field is 1 / factor of whole screen
        factor = 3.5
        field_x = screen_size[0] / 2
        field_y = screen_size[1] / factor
        self.field_size = [field_x, field_y]

        self.Field = stimuli.Canvas(size=self.field_size, position=self.field_position, colour=self.background_colour)

        # Text field for debugging
        if text is not None:
            self.text = text
            text = stimuli.TextBox(self.text, [100,100])
            text.plot(self.Field)

        # Add lines
        self.distance = screen_size[0] / 60
        line_radius = screen_size[0]/10

        for i in range(-2, 3, 1):
            item = {
                'start_point': [-line_radius, self.pos_x - (i * self.distance)],
                'end_point': [line_radius, self.pos_x - (i * self.distance)],
                'line_width': 2,
                'colour': self.foreground_colour
                }
            line = stimuli.Line(item['start_point'], item['end_point'], item['line_width'], colour=item['colour'])
            line.plot(self.Field)

        # Add clef
        clef_pos_x = line_radius * 1.2
        clef = stimuli.Picture('Stimuli/clef_' + design + '_' + clef_name + '.jpg', position=[-clef_pos_x, 0])
        clef.scale(3.9 * screen_size[0] / 100000)
        clef.plot(self.Field)

class Note:
    """
    Implements Note stimulus as expyriment ellipse
    :parameter:
    paradict: dictionary with all stimulus parameters such as key, position_factor, keyboard, cleft, white_key and keyboard pos (see note_info.py)
    midline: optional [int] y-axis offset
    distance: optional [int] distance between lines
        {'key': 'c3',
     'position_factor': 8,
     'keyboard': 'c',
     'clef': 'g',
     'white_key': True,
     'keyboard_pos': 14
    position on screen, name of the note, associated keyboard key, color
    key_name, constants.C_BLACK, item_pos_y, distance

    """
    def __init__(self, paradict, midline=100, distance=30):

        # Assign
        self.pid = paradict['pid']
        self.colour = constants.C_BLACK
        self.key = paradict['key']
        self.key_coded = eval("constants.K_" + paradict['keyboard'])
        self.clef = paradict['clef']
        self.position_factor = paradict['position_factor']
        self.position_y = midline + (self.position_factor * distance / 2)
        self.position = [0, self.position_y]



        # standard values for each note
        self.size = [distance, distance / 2]
        self.stimuli = stimuli.Ellipse(self.size, colour=self.colour, position=self.position)

        self.count = 0
        self.RTs = np.array([])
        self.str_rt = ""
        self.misses = 0
        self.Feedback_text = ""
        self.str_mean = ""

        # Parameter for help lines outsite five music sheet lines
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

    def Evaluate_Buttonpress(self, key_pressed, rt, mouse):

        if mouse:

            if key_pressed == constants.K_SPACE:

                self.Feedback_text = "correct"
                self.RTs = np.append(self.RTs, rt)
                self.str_rt = str("%.1f" % rt)
        else:
            self.Feedback_text = "wrong"
            self.misses += 1
            self.str_rt = ""


        # Calculate mean RT
        if len(self.RTs) > 0:
            self.str_mean = str("%.1f" % np.mean(self.RTs))
        else:
            self.str_mean = ""


class Notes(list):
    """Container for notes.

        Parameters
        ----------
        selection : [str], list of strings, defining the scope of the training (e.g. only f-clef notes)
        pos_y : {int, int}, tuple defining the midline position on the y-axis for each clef
        distance: int, distance between lines
        """
    def appendnotes(self, selection, pos_y, distance):

        for note_info in selection:
            midline = pos_y[note_info['clef']]
            note = Note(note_info, midline, distance)
            self.append(note)


class Feedback:
    """
    Creates Feedback
    """
    def __init__(self, note, settings):

        size_box = settings["size_box"]
        pos_y = settings["position"]
        text_size = settings["text_size"]
        self.text = "Type response: " + note.Feedback_text + "\nRT: " + note.str_rt + "\nMean: " + note.str_mean + "\nMisses: " + str(note.misses)
        self.TextBox = stimuli.TextBox(self.text, size_box, pos_y, text_size=text_size)


class CorrectNote:
    def __init__(self, note, settings):
        size_box = settings["size_box"]
        pos_y = settings["position"]
        text_size = settings["text_size"]

        self.CorrectNote = stimuli.TextBox(note.key, size_box, pos_y, text_size=text_size)


def mouseIsInside (key_size, key_position, mouse_position):

    right = (key_size[0] / 2) + key_position[0]
    left = right - key_size[0]
    top = (key_size[1] / 2) + key_position[1]
    bottom = top - key_size[1]

    mp = mouse_position

    if mp[0] <= right and mp[0] >=  left and mp[1] <= top and mp[1] >= bottom:
        t = True
    else:
        t = False

    return t
