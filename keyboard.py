from expyriment import stimuli
from expyriment.misc import constants
from keys_info import key_mapping

class PianoKey:
    '''
    Class implementing a single piano key as stimulus rectangle
    '''
    def __init__(self, key_mapping):
        self.name = key_mapping['key']
        self.kid = key_mapping['kid']

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


        self.Border = stimuli.Rectangle([width_rect, height_rect], position=position_rect, colour=constants.C_BLACK)
        self.Key = stimuli.Rectangle([width_rect-3, height_rect-3], position=position_rect, colour=colour_rect)
        self.KeyGreen = stimuli.Rectangle([width_rect-3, height_rect-3], position=position_rect, colour=constants.C_GREEN)

        #text parameters
        self.text_title = ""
        y_text = 50
        self.text_position = [x_rect, y_text]



class PianoKeyboard:
    def __init__(self, screen_size, position=[0, 0]):
        self.keys = list()
        self.index = int()
        self.Canvas = stimuli.Canvas([screen_size[0]-100, 200], position, colour=[30, 30, 30])
        self.MouseBool = False
        # fill list of piano keys according to order of appearance in key_info.py
        for iKey in key_mapping:
            k = PianoKey(iKey)
            self.keys.append(k)

        # plot the keys; first all whites and then black on top
        self.whities = [x for x in self.keys if x.white_key]

        self.blackies = [x for x in self.keys if x.white_key == False]

        for iKey in self.whities:
            iKey.Key.plot(self.Canvas)
        for iKey in self.blackies:
            iKey.Key.plot(self.Canvas)


    def evalMouse(self, index, mp):
        # Index goes from right to left
        test_self = self.mouseIsInside(index, mp)
        test_1 = False
        test_2 = False

        if self.keys[index].white_key:
            # Most right key
            if index == 0:
                test_1 = self.mouseIsInside(index+1, mp)
                test_2 = False
            elif index == len(self.keys)-1:
                test_1 = False
                test_2 = self.mouseIsInside(index-1, mp)
            else:
                test_1 = self.mouseIsInside(index+1, mp)
                test_2 = self.mouseIsInside(index-1, mp)

        if test_self is True and (test_1 is False and test_2 is False):
            self.MouseBool = True
        else:
            self.MouseBool = False

    def mouseIsInside(self, index, mouse_position):
        right = (self.keys[index].Key.size[0] / 2) + self.keys[index].Key.position[0]
        left = right - self.keys[index].Key.size[0]
        top = (self.keys[index].Key.size[1] / 2) + self.keys[index].Key.position[1]
        bottom = top - self.keys[index].Key.size[1]

        mp = mouse_position

        if mp[0] <= right and mp[0] >=  left and mp[1] <= top and mp[1] >= bottom:
            t = True
        else:
            t = False

        return t


    def findKey(self, nid):

        count = 0
        for item in self.keys:
            ipid = item.kid
            if ipid == nid:
                return count

            count += 1


    def printColoredKey(self, index):
        """
        prints the expected key in colour. Because black keys overlap white keys, we have to present again the black keys
        left and right to a white key


        :param keys: list of all keys
        :param index: index of the key to be coloured
        :return: nothing

        """


        self.keys[index].KeyGreen.present(clear=False, update=False)

        if self.keys[index].white_key:
            if index == 0:
                ck1 = False
                #ck1 = keys[index+1].Key.present(clear=False, update=False)
            elif index == len(self.keys)-1:
                ck3 = self.keys[index-1].Key.present(clear=False, update=False)
            else:
                ck1 = self.keys[index+1]
                ck3 = self.keys[index-1]
                if ck1.white_key is False:
                    ck1.Key.present(clear=False, update=False)
                if ck3.white_key is False:
                    ck3.Key.present(clear=False, update=False)



    def printKeyName (self, index, name):

        self.Text = stimuli.TextLine(name, self.keys[index].text_position)
        self.Text.present(clear=False, update=True)

