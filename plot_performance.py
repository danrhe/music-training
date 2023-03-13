from settings import Setup
from ggplot import *


setup = Setup([600,480])
data = setup.make_selection(use_all_notes=False)


ggplot(aes(x='note', y='perc'), data=data.bad) + geom_bar(stat='bar')