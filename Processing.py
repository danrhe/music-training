import pandas as pd
#import MySQLdb as db
from credentials import *
from sqlalchemy import *
import numpy as np
import matplotlib.pyplot as plt


engine = create_engine('mysql://' + user_id + ":" + password + '@' + host + '/' + user_db + '?charset=utf8&use_unicode=0', pool_recycle=3600)
con = engine.connect()

#d = db.connect(host, user_id, password, user_db)
data = pd.read_sql_table('Raw', con)
#d.close()

con.close()

pd.pivot_table(data, values='rt', index=['clef', 'note'], columns=['hit'])