from ggplot import *
from Database.use_user_history import User_data

#plt.style.use('ggplot')
#p = ggplot(aes(x='new', y='perc'), data=h) + geom_bar()

#p = ggplot(aes(x='', y='rt', fill='note'), data=Processing.data)

u = User_data('45')
u.get_data()
u.calc_hitrate()
u.get_bad_performance()
