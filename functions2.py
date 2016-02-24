from expyriment import stimuli
from expyriment.misc import constants
import numpy as np
from keys_info import mapping

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
        factor = 4
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
    :param: position on screen, name of the note, associated keyboard key, color

    """
    def __init__(self, position_factor, clef, key, keyboard, colour, midline, distance):

        # Assign
        self.colour = colour
        self.key = key
        self.key_coded = eval("constants.K_" + keyboard)
        self.clef = clef
        self.position_factor = position_factor
        self.position_y = midline + (position_factor * distance / 2)
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
    def Evaluate_Buttonpress (self, key_pressed, rt):

        if  (key_pressed == self.key_coded):
            self.Feedback_text = "correct"
            self.RTs = np.append(self.RTs, rt)
            self.str_rt = str(rt)
        else:
            self.Feedback_text = "wrong"
            self.misses += 1
            self.str_rt = ""


        # Calculate mean RT
        if len(self.RTs) > 0:
            self.str_mean = str(np.mean(self.RTs))
        else:
            self.str_mean = ""


class Notes(list):
    """Container for notes.

        Parameters
        ----------
        clef : [str], list of strings, defining the scope of the training (e.g. only f-clef notes)
        pos_y : {int, int}, tuple defining the midline position on the y-axis for each clef
        distance: int, distance between lines
        """
    def __init__(self, clef, pos_y, distance):
        self = list()

        selection = [x for x in mapping if x['clef'] in clef]

        for item in selection:
            vals = item.values()
            item_pos_y = pos_y[item['clef']]
            vals.extend([constants.C_BLACK, item_pos_y, distance])
            self.append(Note(*vals))


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
    """
    Creates music sheet. This is a composite of white canvas field) with clef and horizontal lines
    """
    def __init__(self, note, settings):
        size_box = settings["size_box"]
        pos_y = settings["position"]
        text_size = settings["text_size"]

        self.CorrectNote = stimuli.TextBox(note.key, size_box, pos_y, text_size=text_size)


