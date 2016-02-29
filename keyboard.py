from expyriment import stimuli
from expyriment.misc import constants
from keys_info import mapping


class PianoKey:
    '''
    Class implementing a single piano key as stimulus rectangle
    '''
    def __init__(self, key_mapping):
        self.name = key_mapping['key']

        # key boarder rectangle parameters
        keys_to_c1 = key_mapping['keyboard_pos']

        x_rect = keys_to_c1 * 20

        self.white_key = key_mapping['white_key']

        if self.white_key:
            #size
            height_rect = 60
            width_rect = 20

            #position
            y_rect = 0
            position_rect = [x_rect, y_rect]

            #colour
            colour_rect = constants.C_WHITE


        else:
            height_rect = 40
            width_rect = 15

            #position
            y_rect = 10
            position_rect = [x_rect, y_rect]

            #colour
            colour_rect = constants.C_BLACK




        #text parameters
        text = self.name
        y_text = 50
        p = [ x_rect, y_text]

        self.Border = stimuli.Rectangle([width_rect, height_rect], position=position_rect, colour=constants.C_BLACK)
        self.Key = stimuli.Rectangle([width_rect-3, height_rect-3], position=position_rect, colour=colour_rect)
        self.KeyGreen = stimuli.Rectangle([width_rect-3, height_rect-3], position=position_rect, colour=constants.C_GREEN)

        self.Text = stimuli.TextLine(text, p)



class PianoKeyboard:
    def __init__(self, screen_size, position=[0, 0]):
        self.keys = list()
        self.Canvas = stimuli.Canvas([screen_size[0]-100, 200], position, colour=[30, 30, 30])

        # fill list of piano keys according to order of appearance in key_info.py
        for iKey in mapping:
            k = PianoKey(iKey)
            self.keys.append(k)

        # plot the keys; first all whites and then black on top
        self.whities = [x for x in self.keys if x.white_key]

        self.blackies = [x for x in self.keys if x.white_key == False]

        for iKey in self.whities:
            iKey.Key.plot(self.Canvas)
        for iKey in self.blackies:
            iKey.Key.plot(self.Canvas)





def findKey(list1, key):
    count = 0
    for item in list1:
        name = item.name
        if name == key:
            return count

        count += 1


def printColoredKey(keys, index):
    """
    prints the expected key in colour. Because black keys overlap white keys, we have to present again the black keys
    left and right to a white key


    :param keys: list of all keys
    :param index: index of the key to be coloured
    :return: nothing

    """


    ck2 = keys[index].KeyGreen.present(clear=False, update=False)

    if keys[index].white_key:
        if index == 0:
            ck1 = keys[index+1].Key.present(clear=False, update=False)
        elif index == len(keys)-1:
            ck3 = keys[index-1].Key.present(clear=False, update=False)
        else:
            ck1 = keys[index+1]
            ck3 = keys[index-1]
            if ck1.white_key is False:
                ck1.Key.present(clear=False, update=False)
            if ck3.white_key is False:
                ck3.Key.present(clear=False, update=False)

    ck = keys[index].Text.present(clear=False, update=True)


    a = 2

