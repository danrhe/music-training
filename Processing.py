import pandas as pd
#import MySQLdb as db
from credentials import *
from sqlalchemy import *
import numpy as np
import matplotlib as plt
from ggplot import *

engine = create_engine('mysql://' + user_id + ":" + password + '@' + host + '/' + user_db + '?charset=utf8&use_unicode=0', pool_recycle=3600)
con = engine.connect()

#d = db.connect(host, user_id, password, user_db)
data = pd.read_sql_table('Raw', con)
#d.close()

con.close()

hit_rate = pd.pivot_table(data, values='rt', index=['clef', 'note'], columns='hit', aggfunc='count')
hit_rate.fillna(0)
hr2 = pd.crosstab([data.clef, data.note],data.hit)
hr2.perc = hr2.correct / (hr2.correct + hr2.wrong) * 100
hr2.perc = hr2.perc.to_frame()
hr2.perc.columns = ['perc']

plt.style.use('ggplot')
hr2.shape()
h = hr2.perc.reset_index()
#d = pd.pivot_table(data, values='rt', index=['clef', 'note'], columns=['hit'])
h['new'] = h['note'] + '_' + h['clef']
#p = ggplot(aes(x='new', y='perc'), data=h) + geom_bar()


#p = ggplot(aes(x='', y='rt', fill='note'), data=Processing.data)