from expyriment import stimuli
############
# Settings #
############
line_dist = 30
white = [255, 255, 255]

class note:
    def __init__(self, position,key, keyboard='K_SPACE',colour=None):

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
        self.RTs = []
        self.misses = 0


settings_canvas = {
    #[SCREEN_WIDTH, SCREEN_HEIGHT]}
    'screen_size': [1680, 1050],
    'colour': [0, 0, 0],
    }

y_init = 120
line_dist = 30

lines = list()
for i in range(-2,3,1):
    lines.append(
        {
        'start_point': [-110, y_init - (i * line_dist)],
        'end_point': [110, y_init - (i * line_dist)],
        'line_width': 3,
        'colour': white,
        })

mapping = [
    {'key': 'f2',
     'position': [0, y_init],
     'keyboard': 'f'
     },
    {'key': 'e2',
     'position': [0, y_init - (1 * line_dist / 2)],
     'keyboard': 'e'
     },
    {'key': 'e1',
     'position': [0, y_init - (8 * line_dist / 2)],
     'keyboard': 'e'
     },
]



