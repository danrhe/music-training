
############
# Settings #
############
line_dist = 30
white = [255, 255, 255]
y_init = 120
nTrials = 10

settings_canvas = {
    # [SCREEN_WIDTH, SCREEN_HEIGHT]}
    'screen_size': [1680, 1050],
    'colour': [0, 0, 0],
    }

lines = list()

mapping = [
    {'key': 'f2',
     'position': [0, y_init + (4 * line_dist / 2)],
     'keyboard': 'f'
     },
    {'key': 'e2',
     'position': [0, y_init + (3 * line_dist / 2)],
     'keyboard': 'e'
     },
    {'key': 'd2',
     'position': [0, y_init + (2 * line_dist / 2)],
     'keyboard': 'd'
     },
    {'key': 'c2',
     'position': [0, y_init + (1 * line_dist / 2)],
     'keyboard': 'c'
     },
    {'key': 'b1',
     'position': [0, y_init + (0 * line_dist / 2)],
     'keyboard': 'b'
     },
    {'key': 'a1',
     'position': [0, y_init + (-1 * line_dist / 2)],
     'keyboard': 'a'
     },
    {'key': 'g1',
     'position': [0, y_init + (-2 * line_dist / 2)],
     'keyboard': 'g'
     },
    {'key': 'f1',
     'position': [0, y_init + (-3 * line_dist / 2)],
     'keyboard': 'f'
     },
    {'key': 'e1',
     'position': [0, y_init + (-4 * line_dist / 2)],
     'keyboard': 'e'
     },
]

